# Deployment Information

## Public URL

TODO: Paste Railway public URL here.

Example:

```text
https://your-chatbot.railway.app
```

## Platform

Railway

## Required Environment Variables

- `GEMINI_API_KEY`: Gemini API key from Google AI Studio
- `LLM_MODEL=gemini-3.1-flash-lite`
- `ENVIRONMENT=production`
- `APP_NAME=Gemini Chatbot`
- `PORT`: provided automatically by Railway

## Railway Commands

```bash
railway login
railway init
railway variables set GEMINI_API_KEY=your-gemini-api-key
railway variables set LLM_MODEL=gemini-3.1-flash-lite
railway variables set ENVIRONMENT=production
railway up
railway domain
```

## Health Check

Railway health check path:

```text
/_stcore/health
```

Expected result: HTTP 200.

## Test

Open the Railway public URL in a browser, type a message in the chat input, and confirm Gemini returns an answer.

## Screenshots

TODO: Add screenshots if required by the instructor.

- Railway variables
- Successful deployment
- Chatbot running
