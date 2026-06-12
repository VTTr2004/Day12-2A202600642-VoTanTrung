import os
import sys


BASE_DIR = os.path.dirname(__file__)


def read_text(path: str) -> str:
    with open(os.path.join(BASE_DIR, path), encoding="utf-8") as file:
        return file.read()


def exists(path: str) -> bool:
    return os.path.exists(os.path.join(BASE_DIR, path))


def check(name: str, passed: bool, detail: str = "") -> bool:
    icon = "OK" if passed else "NO"
    suffix = f" - {detail}" if detail else ""
    print(f"  [{icon}] {name}{suffix}")
    return passed


def main() -> int:
    results: list[bool] = []

    print("\nProduction Readiness Check - Gemini Streamlit Chatbot")
    print("=" * 58)

    print("\nRequired files")
    for path in [
        "app/main.py",
        "app/config.py",
        "app/gemini_client.py",
        "Dockerfile",
        "docker-compose.yml",
        "railway.toml",
        ".env.example",
        "requirements.txt",
    ]:
        results.append(check(f"{path} exists", exists(path)))

    print("\nStreamlit app")
    main_py = read_text("app/main.py") if exists("app/main.py") else ""
    results.append(check("Uses Streamlit chat UI", "st.chat_input" in main_py and "st.chat_message" in main_py))
    results.append(check("Keeps chat history", "st.session_state.messages" in main_py))
    results.append(check("Calls Gemini client", "ask_gemini" in main_py))

    print("\nGemini config")
    config_py = read_text("app/config.py") if exists("app/config.py") else ""
    client_py = read_text("app/gemini_client.py") if exists("app/gemini_client.py") else ""
    env_example = read_text(".env.example") if exists(".env.example") else ""
    results.append(check("Gemini API key from env", "GEMINI_API_KEY" in config_py or "GOOGLE_API_KEY" in config_py))
    results.append(check("Model is Gemini 3.1 Flash-Lite", "gemini-3.1-flash-lite" in config_py + env_example))
    results.append(check("Uses Google Gen AI SDK", "from google import genai" in client_py))
    results.append(check("No hardcoded API key", "AIza" not in config_py + client_py + env_example))

    print("\nDeployment")
    dockerfile = read_text("Dockerfile") if exists("Dockerfile") else ""
    railway = read_text("railway.toml") if exists("railway.toml") else ""
    compose = read_text("docker-compose.yml") if exists("docker-compose.yml") else ""
    results.append(check("Docker starts Streamlit", "streamlit run app/main.py" in dockerfile))
    results.append(check("Railway starts Streamlit", "streamlit run app/main.py" in railway))
    results.append(check("Uses Railway PORT", "$PORT" in railway))
    results.append(check("Streamlit health check configured", "/_stcore/health" in dockerfile + railway))
    results.append(check("Docker Compose exposes 8501", "8501:8501" in compose))

    print("\nDependencies")
    requirements = read_text("requirements.txt") if exists("requirements.txt") else ""
    results.append(check("streamlit dependency", "streamlit" in requirements))
    results.append(check("google-genai dependency", "google-genai" in requirements))
    results.append(check("python-dotenv dependency", "python-dotenv" in requirements))

    passed = sum(results)
    total = len(results)
    pct = round(passed / total * 100)
    print("\n" + "=" * 58)
    print(f"Result: {passed}/{total} checks passed ({pct}%)")
    print("Ready to deploy." if passed == total else "Fix the failed checks above.")
    print("=" * 58 + "\n")

    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
