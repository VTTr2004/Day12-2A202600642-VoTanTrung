# Gemini Streamlit Chatbot

Chatbot don gian dung Streamlit UI va Gemini API, san sang deploy len Railway.

## Cong nghe

- Streamlit cho giao dien chat
- Google Gen AI SDK cho Gemini
- Model mac dinh: `gemini-3.1-flash-lite`
- Docker + Railway config

## Cau truc

```text
06-lab-complete/
├── app/
│   ├── main.py           # Streamlit UI
│   ├── config.py         # Doc bien moi truong
│   └── gemini_client.py  # Goi Gemini API
├── Dockerfile
├── docker-compose.yml
├── railway.toml
├── render.yaml
├── .env.example
└── requirements.txt
```

## Chay local

```bash
cp .env.example .env.local
```

Dien API key vao `.env.local`:

```env
GEMINI_API_KEY=your-gemini-api-key
```

Cai dependencies va chay app:

```bash
pip install -r requirements.txt
streamlit run app/main.py
```

Mo trinh duyet tai:

```text
http://localhost:8501
```

## Chay bang Docker Compose

```bash
docker compose up --build
```

Mo:

```text
http://localhost:8501
```

## Deploy Railway

```bash
npm i -g @railway/cli
railway login
railway init
railway variables set GEMINI_API_KEY=your-gemini-api-key
railway variables set LLM_MODEL=gemini-3.1-flash-lite
railway variables set ENVIRONMENT=production
railway up
railway domain
```

Railway se doc `railway.toml` va chay:

```bash
streamlit run app/main.py --server.address 0.0.0.0 --server.port $PORT
```

Health check cua Streamlit:

```text
/_stcore/health
```
