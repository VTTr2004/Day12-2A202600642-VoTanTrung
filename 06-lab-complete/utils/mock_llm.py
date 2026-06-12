"""
Mock LLM shared by the Day 12 deployment labs.

It avoids requiring a real provider API key while keeping the deployment,
security, health check, and Docker workflow realistic.
"""
import random
import time


MOCK_RESPONSES = {
    "default": [
        "Day la cau tra loi tu AI agent mock. Trong production, day se la response tu OpenAI hoac Anthropic.",
        "Agent dang hoat dong tot. Hay hoi them mot cau nua nhe.",
        "Toi la AI agent duoc deploy len cloud. Cau hoi cua ban da duoc nhan.",
    ],
    "docker": [
        "Container la cach dong goi app de chay nhat quan o nhieu moi truong. Build once, run anywhere."
    ],
    "deploy": [
        "Deployment la qua trinh dua code tu may local len server/cloud de nguoi khac truy cap duoc."
    ],
    "health": [
        "Agent dang hoat dong binh thuong. Health check dang tra ve trang thai on dinh."
    ],
}


def ask(question: str, delay: float = 0.1) -> str:
    """Return a deterministic-enough mock answer with simulated latency."""
    time.sleep(delay + random.uniform(0, 0.05))

    question_lower = question.lower()
    for keyword, responses in MOCK_RESPONSES.items():
        if keyword in question_lower:
            return random.choice(responses)

    return random.choice(MOCK_RESPONSES["default"])


def ask_stream(question: str):
    """Yield a mock response token by token."""
    response = ask(question)
    for word in response.split():
        time.sleep(0.05)
        yield word + " "
