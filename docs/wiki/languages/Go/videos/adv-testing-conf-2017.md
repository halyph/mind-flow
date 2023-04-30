# GopherCon 2017: Advanced Testing with Go by *Mitchell Hashimoto*

## References

- [Video](https://www.youtube.com/watch?v=8hQG7QlcLBk&list=PL2ntRZ1ySWBdD9bru6IR-_WXUgJqvrtx9&index=13)
- [Slides](https://speakerdeck.com/mitchellh/advanced-testing-with-go)

## Table Driven Tests

```go
func TestAdd(t *testing.T) {
	cases := []struct{ A, B, Expected int }{
		{1, 1, 2},
		{1, -1, 0},
		{1, 0, 1},
		{0, 0, 0},
	}
	for _, tc := range cases {
		actual := tc.A + tc.B
		if actual != expected {
			t.Errorf(
				"%d + %d = %d, expected %d",
				tc.A, tc.B, actual, tc.Expected)
		}
	}
}
```

- Low overhead to add new test cases
- Makes testing exhaustive scenarios simple
- Makes reproducing reported issues simple
- Do this pattern a lot
- Follow pattern even for single cases, if its possible to grow

### Consider Naming Cases 

```go
func TestAdd(t *testing.T) {
	cases := map[string]struct{ A, B, Expected int }{
		"foo": {1, 1, 2},
		"bar": {1, -1, 0},
	}
	for k, tc := range cases {
		actual := tc.A + tc.B
		if actual != expected {
			t.Errorf(
				"%s: %d + %d = %d, expected %d",
				k, tc.A, tc.B, actual, tc.Expected)
		}
	}
}
```
or

```go
func TestAdd(t *testing.T) {
	cases := []struct {
		Name           string
		A, B, Expected int
	}{
		{"foo", 1, 1, 2},
		{"bar", 1, -1, 0},
	}

	for k, tc := range cases {
		t.Run(tc.Name, func(t *testing.T) {
			tc.Name
		})
	}
}
```

## Test Fixtures

```go
func TestAdd(t *testing.T) {
	data := filepath.Join("test-fixtures", "add_data.json")
	// ... Do something with data
}
```
- `go test` sets pwd as package directory
- Use relative path `test-fixtures` directory as a place to store test data 
- Very useful for loading config, model data, binary data, etc.

## Golder Files

```go
var update = flag.Bool("update", false, "update golden files")

func TestAdd(t *testing.T) {
	// ... table (probably!)
	for _, tc := range cases {
		actual := doSomething(tc)
		golden := filepath.Join("test-fixtures", tc.Name+".golden")
		if *update {
			ioutil.WriteFile(golden, actual, 0644)
		}
		expected, _ := ioutil.ReadFile(golden)
		if !bytes.Equal(actual, expected) {
			// FAIL!
		}
	}
}
```

```go
$ go test ...
$ go test -update
...
```

- Test complex output without manually hardcoding it
- Human eyeball the generated golden data. If it is correct, commit it
- Very scalable way to test complex structures (write a `String()` method)

## Global State

- Avoid it as much as possible
- Instead of global state, try to make whatever is global a configuration option using global state as the default, allowing tests to modify it
- If necessary, make global state a var so it can be modified. This is a last case scenario, though

```go
// Not good on its own
const port = 1000
// Better
var port = 1000
// Best
const defaultPort = 1000
type ServerOpts struct {
  Port int // default it to defaultPort somewhere
}
```

## Test Helpers

```go
func testTempFile(t *testing.T) string {
	tf, err := ioutil.TempFile("", "test")
	if err != nil {
		t.Fatalf("err: %s", err)
	}
	tf.Close()
	return tf.Name()
}
```

- Never return errors. Pass in `*tesing.T` and fail.
- By not returning errors, usage is much prettier since error checking is gone.
- Used to make tests clear on what they’re tesing vs what is boilerplate
- Call `t.Helper()` for cleaner failuer output (Go 1.9)

```go
func testTempFile(t *testing.T) (string, func()) {
	tf, err := ioutil.TempFile("", "test")
	if err != nil {
		t.Fatalf("err: %s", err)
	}
	tf.Close()
	return tf.Name(), func() { os.Remove(tf.Name()) }
}

func TestThing(t *testing.T) {
	tf, tfclose := testTempFile(t)
	defer tfclose()
}
```

```go
func testChdir(t *testing.T, dir string) func() {
	old, err := os.Getwd()
	if err != nil {
		t.Fatalf("err: %s", err)
	}
	if err := os.Chdir(dir); err != nil {
		t.Fatalf("err: %s", err)
	}
	return func() { os.Chdir(old) }
}

func TestThing(t *testing.T) {
	defer testChdir(t, "/other")()
	// ...
}
```

- Returning a `func()` for cleanup is an elegant way to hide that
- The `func()` is a closure that can have access to `*tesing.T` to also fail
- Example: `testChdir` proper setup/cleanup would be at least 10 lines without the helper. Now avoids that in all our tests.

## Repeat yourself

- Localized logic is more important than test lines of code
- When a test fails, you very often don't remember the details of the test. It is very cumbersome to have logic spread across multiple call sites
- Limit helpers to very reused logic that doesn't fail oftern (example: changing directory) or fails all at once (creating a test server)
- Helpers only help the person who knows they exist and what the do
- copy and paste
- We preder a 200 line test to a 20 line test with abstracted helpers

## Package/Functions

- Break down funcSonality into packages/funcSons judiciously
- NOTE: Don’t overdo it. Do it where it makes sense.
- Doing this correctly will aid testing while also improving organization. Over-doing it will complicate testing and readability.
- Qualitative, but practice will make perfect.
- Unless the function is extremely complex, we try to test only the exported functions, the exported API.
- We treat unexported functions/structs as implementation details: they are a means to an end. As long as we test the end and it behaves within spec, the means don’t matter.
- Some people take this too far and choose to only integration/acceptance test, the ultimate "test the end, ignore the means". We disagree with this approach.


## Internal Packages

- Use internal packages to safely "over-package"
- Uder-packaging is very hard to refactor out in small pieces due to import cycle. You really have to do a major refactor.
- We prefer to create *too many packages* (many only export a single fucntion) and hide then under "internal" just in case.

## Networking

- Testing networking? Make a real network connection. 
- Don’t mock `net.Conn`, no point.

```go
// Error checking omitted for brevity
func TestConn(t *testing.T) (client, server net.Conn) {
	ln, err := net.Listen("tcp", "127.0.0.1:0")
	var server net.Conn
	go func() {
		defer ln.Close()
		server, err = ln.Accept()
	}()
	client, err := net.Dial("tcp", ln.Addr().String())
	return client, server
}
```

- That was a one-connectionon example. Easy to make an N-connection. Easy to test any protocol.
- Easy to return the listener as well.
- Easy to test IPv6 if needed.
- Why ever mock `net.Conn`? (Rhetorical, for readers)

## Configurability

- Unconfigurable behavior is often a point of difficulty for tests
	- Example: ports, timeouts, paths
- Over-parameterize structs to allow tests to fine-tune their behavior
- It is okay to make these configurations unexported so only tests can set them

```go
// Do this, even if cache path and port are always the same
// in practice. For testing, it lets us be more careful.
type ServerOpts struct {
	CachePath string
	Port      int
}
```

```go
type ServerOpts struct {
	// ...
	
	// Enables test mode which changes the behavior by X, Y, Z
	Test bool
}
```

## Complex Structs

```go
type ComplexThing struct { /* ... */ }

func (c *ComplexThing) testString() string {
	// produce human-friendly output for test comparison
}

// ----------------------

func TestComplexThing(t *testing.T) {
	c1, c2 := createComplexThings()
	if c1.testString() != c2.testString() {
		t.Fatalf("no match:\n\n%s\n\n%s", c1.testString(), c2.testString())
	}
}
```

- Trees, linked lists, etc. Example: Terraform graphs!
- Can use `reflect.DeepEqual` or 3rd party lib
- Can sometimes produce better output and test more specific functionality with `testString()`
- A bit blunt honestly but we've had good results

```go
const testSingleDepStr = `
root: root
aws_ instance.bar
	awS.instance.bar -> provider.aws
aws_instance.foo
	aws_instance.foo -> provider.aws
provider.aws
root
	root -> aws_instance.bar
	root -> aws_instance.foo
`
```

## Subprocessing

- Subprocessing is typical a point of difficult-to-test behavior.
- Two options:
	- 1. Actually do the subprocess 
	- 2. Mock the output or behavior

### Subprocessing: Real

- Actually executing the subprocess is nice
- Guard the test for the existence of the binary 
- Make sure side effects don’t affect any other test

```go
var testHasGit bool

func init() {
	if _, err := exec.LookPath("git"); err == nil {
		testHasGit = true
	}
}
func TestGitGetter(t *testing.T) {
	if !testHasGit {
		t.Log("git not found, skipping")
		t.Skip()
	}
	// ...
}
```

### Subprocessing: Mock


- You still actually execute, but you’re executing a mock! 
- Make the `*exec.Cmd` configurable, pass in a custom one 
- Found this in the stdlib, it is how they test `os/exec`! 
- How HashiCorp tests go-plugin and more

#### Get the `exec.Command`

```go
func helperProcess(s ...string) *exec.Cmd {
	cs := []string{"-test.run=TestHelperProcess", "--"}
	cs = append(cs, s...)
	env := []string{
		"GO_WANT_HELPER_PROCESS=1",
	}
	cmd := exec.Command(os.Args[0], cs...)
	cmd.Env = append(env, os.Environ()...)
	return cmd
}
```

#### What it  executes

```go
func TestHelperProcess(*testing.T) {
	if os.Getenv("GO_WANT_HELPER_PROCESS") != "1" {
		return
	}
	defer os.Exit(0)
	args := os.Args
	for len(args) > 0 {
		if args[0] == "--" {
			args = args[1:]
			break
		}
		args = args[1:]
	}
}
```

```go
cmd, args := args[0], args[1:]
switch cmd {
case “foo”:
	// ...
```


## Interfaces

- Interfaces are mocking points.
- Behavior can be defined regardless of implementaSon and exposed via custom framework or tesing.go (covered elsewhere)
- Similar to package/functions: do this judiciously, but overdoing it will complicate readability
- Use smaller interfaces where they make sense
- If you have a big interface that is also an `io.Closer` but for a function
you only need the Close function, take only the `io.Closer`.
- Simplifies testing since a smaller mock interface can be implemented

```go
func ServeConn(rwcio.ReadWriteCloser) error {
	// ...
}

func main() {
	conn, err = net.Dial("tcp", "127.0.0.1")
	ServeConn(conn)
}
```


## Testing as a Public API

- Newer HashiCorp projects have adopted the practice of making a `testing.go` or `testing_*.go` files
- These are exported APIs for the sole purpose of providing mocks, test harnesses, helpers, etc.
- Allows other packages to test using our package without reinventing the components needed to meaningful use our package in a test

### Examples

- Example: config file parser
	- `TestConfig(t)` => Returns a valid, complete configuration for tests
	- `TestConfigInvalid(t)` => Returns an invalid configuraSon
- Example: API server
	- `TestServer(t) (net.Addr, io.Closer)` => Returns a fully started in-memory server (address to connect to) and a closer to close it.
- Example: interface for downloading files
	- `TestDownloader(t, Downloader)` => Tests all the properties a downloader should have.
	- `struct DownloaderMock{}` => Implements Downloder as a mock, allowing recording and replaying of calls.

See:
- [github.com/mitchellh/go-testing-interface](github.com/mitchellh/go-testing-interface) for `testing.T` interface
- Using the real "testing" package will modify global state (adds flags to
the global flag), and allows testing your test APls!

```go
import "github.com/mitchellh/go-testing-interface"
// NOTE: non-pointer, cause its not the real "testing" package
func TestConfig(t testing.T) {
	t.Fatal("fail!")
}
```

## Custom Frameworks

- `go test` is an incredible workflow tool
- Complex, pluggable systems? Write a custom framework within `go test`, rather than a separate test harness.
- Example: Terraform providers, Vault backends, Nomad schedulers

```go
// Example from Vault
func TestBackend_basic(t *testing.T) {
	b, _ := Factory(logical.TestBackendConfig())
	logicaltest.Test(t, logicaltest.TestCase{
		PreCheck: func() { testAccPreCheck(t) },
		Backend:  b,
		Steps: []logicaltest.TestStep{
			testAccStepConfig(t, false),
			testAccStepRole(t),
			testAccStepReadCreds(t, b, "web"),
			testAccStepConfig(t, false),
			testAccStepRole(t),
			testAccStepReadCreds(t, b, "web"),
		}})
}
```
 
- `logicaltest.Test` is just a custom harness doing repeated setup/teardown, assertions, etc.
- Other examples: Terraform provider acceptance tests 
- We can still use `go test` to run them

## Timing-dependent tests

```go
func TestThing(t *testing.T) {
	// ...
	select {
	case <-thingHappened:
	case <-time.After(timeout):
		t.Fatal("timeout")
	}
}
```

- We don’t use “fake time”
- We just have a multiplier available that we can set to increase timeouts
- Not perfect, but not as intrusive as fake time. Still, fake time could be better, but we haven’t found an effective way to use it yet.

```go
func TestThing(t *testing.T) {
  // ...
  timeout := 3 * time.Minute * timeMultiplier
  select {
  case <-thingHappened:
  case <-time.After(timeout):
    t.Fatal(“timeout”)
  }
}
```

## Parallelization

```go
func TestThing(t *testing.T) {
	t.Parallel()
}
```

- Don’t do it. Run multiple processes
- Makes test failures uncertain: is it due to pure logic but, or race? 
- *OR*: Run tests both with `-parallel=1` and `-parallel=N`
- We’ve preferred to just not use parallelization. We use multiple processes and unit tests specifically written to test for races.
