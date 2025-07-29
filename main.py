import streamlit as st
from openai import OpenAI

# Set your API key and base URL
YOUR_API_KEY = "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"
client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

# Streamlit app UI
st.set_page_config(page_title="Hema Chatbot", layout="centered")
st.title("🤖 Chat with Hema")

# Text input for user message
user_input = st.text_input("You:", placeholder="Ask me anything...")

if st.button("Send") and user_input:
    with st.spinner("Hema is thinking..."):
        messages = [
            {
                "role": "system",
                "content": (
                    "You are Hema, a friendly, witty, and wise AI assistant. "
                    "Engage with the user in a warm and helpful manner."
                ),
            },
            {
                "role": "user",
                "content": user_input
            },
        ]

        try:
            response = client.chat.completions.create(
                model="sonar-pro",
                messages=messages,
                stream=False
            )
            assistant_reply = response.choices[0].message.content
            st.markdown(f"**Hema:** {assistant_reply}")
        except Exception as e:
            st.error(f"Error: {e}")
