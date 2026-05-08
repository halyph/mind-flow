# Building Resilient HTTP Clients in Go: A Middleware Journey
<!-- tags: golang -->

![thumbnail](2026-05-08-go-middleware/pic0.jpg)

Building reliable HTTP clients means handling failures gracefully. This post shows how a simple retry middleware evolved into a robust three-layer system: *Cache*, *Retry*, and *RateLimitRetry*.

## The Starting Point: Basic Retry

Initially, we had just retry logic with exponential backoff:

```go
func createHTTPClient(tracer trace.Tracer, timeout time.Duration) *http.Client {
    baseClient := &http.Client{Timeout: timeout}
    
    return middleware.WrapClient(baseClient,
        middleware.Retry(middleware.RetryConfig{
            MaxRetries: 3,
            Backoff: middleware.NewExponentialBackoff(
                500*time.Millisecond, // Initial interval
                5*time.Second,        // Max interval
                30*time.Second,       // Max elapsed time
            ),
            Tracer: tracer,
        }),
    )
}
```

This handles transient failures (5xx errors) but has limitations:

- Every request hits the external API
- Rate limits (429) get treated like any other retry
- No awareness of `Retry-After` headers

## The Evolution: Adding Cache + RateLimitRetry

The enhanced version adds two specialized middleware layers:

```go
func createHTTPClient(tracer trace.Tracer, timeout time.Duration) *http.Client {
    baseClient := &http.Client{Timeout: timeout}
    
    return middleware.WrapClient(baseClient,
        middleware.Cache(middleware.CacheConfig{
            TTL:    10 * time.Second,
            Tracer: tracer,
        }),
        middleware.Retry(middleware.RetryConfig{
            MaxRetries: 3,
            Backoff: middleware.NewExponentialBackoff(
                500*time.Millisecond,
                5*time.Second,
                30*time.Second,
            ),
            Tracer: tracer,
        }),
        middleware.RateLimitRetry(middleware.RateLimitRetryConfig{
            MaxRetries:        2,
            MaxRetryAfterWait: 10 * time.Second,
            DefaultRetryAfter: 2 * time.Second,
            Tracer:            tracer,
        }),
    )
}
```

**Middleware order matters**: Cache → Retry → RateLimitRetry

## Why This Design?

**Cache first** - When a response is cached, the request never reaches retry or rate limit layers. Cache hits return in ~1ms vs 100ms+ for API calls.

**RateLimitRetry** - HTTP 429 isn't a failure, it's intentional throttling. The `Retry-After` header tells you exactly when to retry - no guessing with exponential backoff. For 5xx errors, it passes through to the general Retry middleware.

**Separation of concerns** - Each middleware handles one failure type. OpenTelemetry tracing shows exactly which layer handled each request.

## Scenarios: The Middleware in Action

All scenarios use the complete middleware chain shown above.

### Scenario 0: Baseline

![Scenario 0 - Baseline](2026-05-08-go-middleware/scenario-0-baseline.png)

Happy path - request flows through all layers, succeeds.

### Scenario 1: Cache Hit/Miss

![Scenario 1 - Cache Demo](2026-05-08-go-middleware/scenario-1-cache-demo.png)

First request (MISS): 150ms. Second request (HIT): instant.

### Scenario 2: Retry with 5xx

![Scenario 2 - Retry Demo](2026-05-08-go-middleware/scenario-2-retry-demo.png)

Server returns 500 twice, then succeeds with exponential backoff.

### Scenario 3: Rate Limit Handling

![Scenario 3 - Rate Limit Demo](2026-05-08-go-middleware/scenario-3-ratelimit-demo.png)

429 with `Retry-After: 2` → waits 2s → retries → succeeds.

### Scenario 4: Rate Limit Exhaustion

![Scenario 4 - Rate Limit Exhausted](2026-05-08-go-middleware/scenario-4-ratelimit-exhausted.png)

Persistent 429s exhaust retry limit, fails gracefully.

### Scenario 5: 5xx Passes Through

![Scenario 5 - 5xx Retry](2026-05-08-go-middleware/scenario-5-retry-5xx.png)

RateLimitRetry passes 5xx to Retry (no RateLimitRetry spans). Success gets cached.

### Scenario 6: Timeout

![Scenario 6 - Timeout Demo](2026-05-08-go-middleware/scenario-6-timeout-demo.png)

Client timeout exceeded - fails fast, no retry.

## See It in Action

Want to see how these middleware patterns work in real code?  
The complete implementation with a live demo is ready to run: **[mindflow-http-middleware-patterns](https://github.com/halyph/mindflow-http-middleware-patterns)**

### What You Get

- **Production-ready middleware** - *Cache*, *Retry*, and *RateLimitRetry* using battle-tested libraries ([jellydator/ttlcache](https://github.com/jellydator/ttlcache), [cenkalti/backoff](https://github.com/cenkalti/backoff))
- **Visual debugging** - OpenTelemetry traces show exactly how requests flow through the middleware layers
- **7 interactive scenarios** - See cache hits, exponential backoff, rate limit handling, and edge cases in action

### Run the Demo

One command launches everything: 

```shell
make demo
```

This builds binaries, starts Jaeger, executes all 7 scenarios, and opens the trace UI. The sequence diagrams in this post? They come straight from those traces.

Perfect for understanding middleware patterns visually or adapting the code for your own projects.

