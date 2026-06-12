# Day 12 Lab - Mission Answers

## Part 1: Localhost vs Production

### Exercise 1.1: Anti-patterns Found

1. Hardcoded secrets such as API keys should not be stored in source code.
2. Hardcoded host, port, debug mode, and model settings make deployment harder.
3. A local-only app usually has no health endpoint for cloud platforms.
4. Running without authentication is unsafe once the API has a public URL.
5. Keeping state only in memory makes scaling and restarts unreliable.

### Exercise 1.3: Comparison Table

| Feature | Develop | Production | Why Important? |
|---|---|---|---|
| Config | Values may be local defaults | Values come from environment variables | Same code can run across local, staging, and cloud |
| Secrets | Sometimes copied into local files | Stored in platform secret manager/env vars | Prevents leaking keys in Git |
| Debug | Can be enabled | Disabled | Avoids exposing internals |
| Health checks | Optional | Required | Cloud platform can detect failed containers |
| Logging | Human-readable logs | Structured JSON logs | Easier to search and monitor |

## Part 2: Docker

### Exercise 2.1: Dockerfile Questions

1. Base image: `python:3.11-slim`.
2. Working directory: `/app` in runtime and `/build` in builder.
3. Dependencies are installed in a builder stage, then copied into the runtime image.
4. The app runs as a non-root `agent` user.
5. The container exposes port `8000`.
6. The container includes a `HEALTHCHECK` calling `/health`.

### Exercise 2.3: Image Size Comparison

- Develop: TODO if measured during class.
- Production: TODO if measured during class.
- Difference: The production image should be smaller and safer because it uses a slim base image, multi-stage build, `.dockerignore`, and a non-root runtime user.

## Part 3: Cloud Deployment

### Exercise 3.1: Railway or Render Deployment

- URL: TODO paste deployed URL.
- Platform: TODO Railway or Render.
- Result: The app should respond successfully on `/health` and require `X-API-Key` for `/ask`.

## Part 4: API Security

### Exercise 4.1: Authentication Test

Without `X-API-Key`, `POST /ask` returns HTTP 401.

### Exercise 4.2: Authenticated Request

With the correct `X-API-Key`, `POST /ask` returns HTTP 200 and a JSON response containing the question, answer, model, and timestamp.

### Exercise 4.3: Rate Limiting

The app keeps a rolling one-minute window per API key bucket. If requests exceed `RATE_LIMIT_PER_MINUTE`, it returns HTTP 429 with a `Retry-After` header.

### Exercise 4.4: Cost Guard Implementation

The app estimates input and output tokens from word count, calculates approximate LLM cost, tracks daily spend, and returns HTTP 503 when `DAILY_BUDGET_USD` is exhausted.

## Part 5: Scaling & Reliability

### Exercise 5.1: Health Check

`GET /health` returns app status, version, environment, uptime, request count, dependency check, and timestamp.

### Exercise 5.2: Readiness Check

`GET /ready` returns `{"ready": true}` only after startup initialization finishes.

### Exercise 5.3: Graceful Shutdown

The app uses FastAPI lifespan events and handles `SIGTERM`, allowing the platform to stop containers cleanly.

### Exercise 5.4: Stateless Design

The API does not depend on local files or per-process conversation memory for core request handling. Production state should be moved to Redis or another external store when persistent state is needed.

### Exercise 5.5: Reliability Notes

The deployment includes Docker health checks, cloud health check configuration, environment-based config, protected metrics, CORS configuration, and security headers.

## Part 6: Final Project

The final project in `06-lab-complete` includes:

- FastAPI app with `/ask`, `/health`, `/ready`, and `/metrics`.
- API key authentication.
- Rate limiting.
- Daily cost guard.
- Environment variable configuration.
- Structured logging.
- Graceful shutdown.
- Multi-stage Dockerfile.
- Docker Compose stack with Redis.
- Railway and Render deployment config.
