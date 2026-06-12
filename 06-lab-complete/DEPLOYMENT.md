# Deployment Information

## Public URL

TODO: Paste the public service URL from Railway or Render here.

Example:

```text
https://your-agent.railway.app
```

## Platform

TODO: Railway or Render.

## Test Commands

Replace `<PUBLIC_URL>` and `<AGENT_API_KEY>` with the real values from the deployed service.

### Health Check

```bash
curl <PUBLIC_URL>/health
```

Expected result: HTTP 200 with JSON containing `"status": "ok"`.

### Readiness Check

```bash
curl <PUBLIC_URL>/ready
```

Expected result: HTTP 200 with JSON containing `"ready": true`.

### Authentication Required

```bash
curl -X POST <PUBLIC_URL>/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Hello"}'
```

Expected result: HTTP 401 because `X-API-Key` is missing.

### API Test With Authentication

```bash
curl -X POST <PUBLIC_URL>/ask \
  -H "X-API-Key: <AGENT_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is deployment?"}'
```

Expected result: HTTP 200 with an agent answer.

### Metrics

```bash
curl <PUBLIC_URL>/metrics \
  -H "X-API-Key: <AGENT_API_KEY>"
```

Expected result: HTTP 200 with uptime, request count, error count, and budget usage.

## Environment Variables Set

- `ENVIRONMENT=production`
- `APP_VERSION=1.0.0`
- `OPENAI_API_KEY` optional for this mock lab
- `AGENT_API_KEY`
- `JWT_SECRET`
- `DAILY_BUDGET_USD=10.0`
- `RATE_LIMIT_PER_MINUTE=10`
- `PORT` provided by the cloud platform

## Screenshots

TODO: Add screenshots if required by the instructor.

- Deployment dashboard
- Service running
- Health check result
- Authenticated `/ask` result
