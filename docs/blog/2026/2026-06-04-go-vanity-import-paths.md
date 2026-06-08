# Go Vanity Import Paths
<!-- tags: golang -->

![thumbnail](2026-06-04-go-vanity-import-paths/pic0.jpg)

I've been seeing these import paths in Go projects:

- `go.uber.org/zap`
- `k8s.io/client-go`
- `go.opentelemetry.io/otel`
- `google.golang.org/grpc`

These aren't GitHub URLs. How does Go resolve them? I decided to investigate.

## The Investigation

First, I checked what these domains actually return:

```shell
$ curl go.uber.org/zap
<!DOCTYPE html>
<html>
    <head>
        <meta name="go-import" content="go.uber.org/zap git https://github.com/uber-go/zap">
        <meta name="go-source" content="go.uber.org/zap https://github.com/uber-go/zap https://github.com/uber-go/zap/tree/master{/dir} https://github.com/uber-go/zap/tree/master{/dir}/{file}#L{line}">
        <meta http-equiv="refresh" content="0; url=https://pkg.go.dev/go.uber.org/zap">
    </head>
    <body>
        Nothing to see here. Please <a href="https://pkg.go.dev/go.uber.org/zap">move along</a>.
    </body>
</html>
```

Interesting. Just HTML with meta tags pointing to GitHub. Same pattern everywhere.

## The Official Docs

Found the explanation in [Remote import paths](https://pkg.go.dev/cmd/go#hdr-Remote_import_paths):

> If the import path is not a known code hosting site and also lacks a version control qualifier, the go tool attempts to fetch the import over https/http and looks for a `<meta>` tag in the document's HTML `<head>`.
>
> The meta tag has the form:
>
> ```html
> <meta name="go-import" content="import-prefix vcs repo-root">
> ```

**Note**: Go adds `?go-get=1` to the request so servers can distinguish between Go tooling and regular browsers.

So the flow is:

1. Go requests `https://go.uber.org/zap?go-get=1`
2. Parses `go-import` meta tag from HTML `<head>`
3. Clones from actual repository: `https://github.com/uber-go/zap`

Simple HTTP + HTML meta tags. No magic.

## Who Uses This

I checked several major Go projects:

- **Kubernetes** - `k8s.io/*` → [`github.com/kubernetes/*`](https://github.com/kubernetes)
- **gRPC** - `google.golang.org/grpc` → [`github.com/grpc/grpc-go`](https://github.com/grpc/grpc-go)
- **Uber** - `go.uber.org/*` → [`github.com/uber-go/*`](https://github.com/uber-go)
- **OpenTelemetry** - `go.opentelemetry.io/*` → [`github.com/open-telemetry/*`](https://github.com/open-telemetry)
- **etcd** - `go.etcd.io/*` → [`github.com/etcd-io/etcd`](https://github.com/etcd-io/etcd)
- **Knative** - `knative.dev/*` → [`github.com/knative/*`](https://github.com/knative)

All large organizations with many packages. Makes sense - if you're managing 20+ Go repos, a custom domain gives you VCS flexibility.

## The Go Implementation

I wanted to see how Go actually implements this. Found it in the Go source at `src/cmd/go/internal/vcs/`:

**Building the URL** (`vcs.go`):

```go
func urlForImportPath(importPath string) (*url.URL, error) {
    host, path := splitPath(importPath)
    return &url.URL{Host: host, Path: path, RawQuery: "go-get=1"}, nil
}
```

Turns `go.uber.org/zap` → `https://go.uber.org/zap?go-get=1`.

**Parsing HTML** (`discovery.go`):

```go
func parseMetaGoImports(r io.Reader) ([]metaImport, error) {
    decoder := xml.NewDecoder(r)
    decoder.Strict = false // Lenient parsing
    
    // Scan for <meta name="go-import" content="...">
    // Stop at </head> or <body>
}
```

Key details: case-insensitive HTML parsing, only scans `<head>` section, caches results, and has built-in patterns for GitHub/Bitbucket.

## How to Implement It

**Option 1: Static HTML** (what most orgs use)

Host a simple HTML file on your custom domain:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta name="go-import" content="example.com/pkg git https://github.com/you/pkg">
    <meta http-equiv="refresh" content="0; url=https://pkg.go.dev/example.com/pkg">
  </head>
  <body>
    Nothing to see here. Please <a href="https://pkg.go.dev/example.com/pkg">move along</a>.
  </body>
</html>
```

Host it on GitHub Pages or Netlify (both free with custom domains).

**Option 2: Dynamic Server**

Check the `?go-get=1` parameter:

```go
func handler(w http.ResponseWriter, r *http.Request) {
    if r.URL.Query().Get("go-get") == "1" {
        // Go tooling gets meta tags
        w.Header().Set("Content-Type", "text/html")
        fmt.Fprintf(w, `<meta name="go-import" content="example.com/pkg git https://github.com/you/pkg">`)
        return
    }
    // Humans get redirected
    http.Redirect(w, r, "https://pkg.go.dev/example.com/pkg", http.StatusFound)
}
```

This is what Google uses for `google.golang.org/grpc`.

**Existing Tools:**

- [vangen](https://github.com/leighmcculloch/vangen) - Generate static HTML
- [sally](https://github.com/uber-go/sally) - Uber's production server

## When It Makes Sense

After looking at who uses vanity import paths, the pattern is clear:

| Use Case | Makes Sense? |
|----------|--------------|
| Large org with 10+ packages | ✓ |
| Might migrate from GitHub to GitLab | ✓ |
| Professional branding needed | ✓ |
| Small personal project (1-3 repos) | ✗ |
| Internal-only packages | ✗ |
| GitHub URL is already clean | ✗ |

I'd say if you're managing fewer than 5 packages and don't plan to move VCS providers, stick with GitHub URLs. The overhead isn't worth it.

But if you're Uber with 50+ Go repos, having them all under `go.uber.org/*` makes a lot of sense.

## The Elegance

Vanity import paths are beautifully simple: HTML meta tags + HTTP redirects. No complex infrastructure.

The clever bit? Same endpoint, different behavior:

1. **Go tooling** (`?go-get=1`) → reads meta tags → clones from GitHub
2. **Humans** (no parameter) → redirected to documentation

It's **optional** for GitHub but **available** for custom domains. Only use it when you need it.

The real win: migrate from GitHub → GitLab → self-hosted without breaking downstream imports. Maximum flexibility, minimal code.

## References

- [Remote import paths](https://pkg.go.dev/cmd/go#hdr-Remote_import_paths) - Official spec
- [Module VCS Discovery](https://go.dev/ref/mod#vcs-find) - How Go discovers repositories
- [Vanity Import Paths in Go](https://sagikazarmark.hu/blog/vanity-import-paths-in-go/) - Comprehensive guide
- Go source: [`discovery.go`](https://github.com/golang/go/blob/master/src/cmd/go/internal/vcs/discovery.go), [`vcs.go`](https://github.com/golang/go/blob/master/src/cmd/go/internal/vcs/vcs.go)

## Appendix: The Caching Implementation

I mentioned Go caches the meta tag results. I was curious how that actually works, so I looked at the implementation in `vcs.go`:

```go
// Global cache and mutex for thread-safe access
var (
    fetchCacheMu sync.Mutex
    fetchCache   = map[string]fetchResult{} // key is the import prefix
)

var fetchGroup singleflight.Group // Deduplicates concurrent requests

func metaImportsForPrefix(importPrefix string, ...) (*url.URL, []metaImport, error) {
    setCache := func(res fetchResult) (fetchResult, error) {
        fetchCacheMu.Lock()
        defer fetchCacheMu.Unlock()
        fetchCache[importPrefix] = res
        return res, nil
    }

    // Use singleflight to deduplicate concurrent requests
    resi, _, _ := fetchGroup.Do(importPrefix, func() (resi any, err error) {
        // Check cache first
        fetchCacheMu.Lock()
        if res, ok := fetchCache[importPrefix]; ok {
            fetchCacheMu.Unlock()
            return res, nil  // Cache hit!
        }
        fetchCacheMu.Unlock()

        // Cache miss - fetch from URL
        url, err := urlForImportPath(importPrefix)
        resp, err := web.Get(security, url)
        defer resp.Body.Close()
        
        imports, err := parseMetaGoImports(resp.Body, mod)
        return setCache(fetchResult{url: url, imports: imports, err: err})
    })
}
```

**Two-level deduplication:**

1. **Singleflight** - If 10 goroutines request `go.uber.org/zap` simultaneously, only ONE HTTP request is made. Others wait for the result.
2. **Simple map cache** - Once fetched, subsequent requests for `go.uber.org/zap` return cached results immediately (no HTTP call).

**Example flow:**

```go
// First request: go.uber.org/zap
fetchCache = {} // empty
// → HTTP request to https://go.uber.org/zap?go-get=1
// → Store: {"go.uber.org/zap": {url, imports, err}}

// Second request: go.uber.org/zap
fetchCache = {"go.uber.org/zap": {...}}
// → Return cached result (no HTTP request)

// Concurrent requests:
// goroutine 1: requests go.uber.org/zap (makes HTTP call)
// goroutine 2: requests go.uber.org/zap (waits for goroutine 1)
// goroutine 3: requests go.uber.org/zap (waits for goroutine 1)
// → All three get the same result, only one HTTP request
```

The cache lives in memory for the duration of the `go` command execution. Not persisted to disk.

Simple but effective - prevents hammering vanity domains during dependency resolution.
