import sys
from pathlib import Path

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.config import settings
from app.gemini_client import ask_gemini


st.set_page_config(
    page_title=settings.app_name,
    page_icon=":speech_balloon:",
    layout="centered",
)


def init_messages() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Xin chao! Minh la chatbot Gemini. Ban muon hoi gi hom nay?",
            }
        ]


def render_sidebar() -> None:
    with st.sidebar:
        st.title("Cau hinh")
        st.caption(f"Model: `{settings.llm_model}`")
        st.caption(f"Moi truong: `{settings.environment}`")

        if not settings.gemini_api_key:
            st.warning(
                "Chua co GEMINI_API_KEY/GOOGLE_API_KEY. Hay them bien moi truong tren Railway."
            )

        if st.button("Xoa lich su chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()


def build_prompt(messages: list[dict[str, str]]) -> str:
    recent_messages = messages[-12:]
    lines = [
        "Ban la mot tro ly AI huu ich, tra loi ngan gon, ro rang bang tieng Viet.",
        "Neu nguoi dung hoi bang ngon ngu khac, hay tra loi theo ngon ngu do.",
        "",
        "Lich su hoi thoai:",
    ]
    for message in recent_messages:
        role = "Nguoi dung" if message["role"] == "user" else "Tro ly"
        lines.append(f"{role}: {message['content']}")
    return "\n".join(lines)


init_messages()
render_sidebar()

st.title(settings.app_name)
st.caption("Chatbot Streamlit dung Gemini 3.1 Flash-Lite, san sang deploy len Railway.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Nhap cau hoi cua ban..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Dang suy nghi..."):
            try:
                answer = ask_gemini(build_prompt(st.session_state.messages))
            except Exception as exc:
                answer = f"Co loi khi goi Gemini: `{exc}`"
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
