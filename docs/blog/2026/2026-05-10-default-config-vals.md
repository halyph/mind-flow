# Default Config Values are Actually Hidden Landmines
<!-- tags: golang, thoughts -->

![thumbnail](2026-05-10-default-config-vals/pic0.jpg)

## The Setup

```go
// config.go
func Load() Application {
	return Application{
		//...
		PrimaryAPI: PrimaryAPI{
			ApplicationID: EnvString("PRIMARY_API_APPLICATION_ID", "example-primary-api"),
			BaseURL:       EnvURL("PRIMARY_API_BASE_URL", "http://primary-service-test.mycomp.com"),
			TokenName:     EnvString("PRIMARY_API_TOKEN_NAME", "example-primary-api-write"),
		},
		SecondaryAPI: SecondaryAPI{
			ApplicationID: EnvString("SECONDARY_API_APPLICATION_ID", "example-secondary-api"),
			BaseURL:       EnvURL("SECONDARY_API_BASE_URL", "http://secondary-service-test.mycomp.com"),
			TokenName:     EnvString("SECONDARY_API_TOKEN_NAME", "example-secondary-api-write"),
		},
		// ...
	}
}
```

### What Happened

A developer deployed a new service with several external API dependencies. The **BaseURL**s had default values pointing to TEST environment. Deployment succeeded, the service ran without errors, and everything looked fine.

Day later, we discovered data inconsistencies in PROD. The root cause: our service was silently calling TEST APIs from the PROD environment. TEST doesn't have access to PROD services, but PROD can reach TEST (network asymmetry). So PROD was happily fetching stale test data instead of production data.

The deployment succeeded because the **BaseURL**s had defaults. No missing environment variables meant no startup failures. The configuration quietly fell back to TEST URLs.

## The Fix

If a config value points to infrastructure (Database, API, Event Stream), it must be explicit - no defaults allowed.  

```go
// config.go
func Load() Application {
	return Application{
		//...
		PrimaryAPI: PrimaryAPI{
			ApplicationID: EnvString("PRIMARY_API_APPLICATION_ID", "example-primary-api"),
			BaseURL:       MustEnvURL("PRIMARY_API_BASE_URL"),
			TokenName:     EnvString("PRIMARY_API_TOKEN_NAME", "example-primary-api-write"),
		},
		SecondaryAPI: SecondaryAPI{
			ApplicationID: EnvString("SECONDARY_API_APPLICATION_ID", "example-secondary-api"),
			BaseURL:       MustEnvURL("SECONDARY_API_BASE_URL"),
			TokenName:     EnvString("SECONDARY_API_TOKEN_NAME", "example-secondary-api-write"),
		},
		// ...
	}
}

// MustEnvURL returns URL from env var, panics if missing.
func MustEnvURL(key string) *url.URL {
	value := os.Getenv(key)
	if value == "" {
		panic(fmt.Sprintf("missing required environment variable '%s'", key))
	}

	u, err := url.Parse(value)
	if err != nil {
		panic(fmt.Sprintf("unable to convert %v to a url value", value))
	}

	return u
}
```

## When Defaults Are Fine

Defaults work well for operational settings:

- **Application behavior**: Log levels, timeouts, retry counts, page sizes
- **Development ergonomics**: Debug flags, verbose mode, pretty-print
- **Feature flags**: New features off by default
- **Non-critical integrations**: Analytics, telemetry

These control **how** you communicate, not **which system** you target.

| Type | Example |
|------|---------|
| **✓ Safe** | `RetryAttempts: EnvInt("RETRY_ATTEMPTS", 3)` |
| **✗ Dangerous** | `BaseURL: EnvURL("API_BASE_URL", "https://api-test.company.com")` |

Rule: require config that determines infrastructure targets (fail-fast at startup) and allow defaults for operational behavior.
