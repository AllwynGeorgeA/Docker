import os
import requests
import streamlit as st


st.set_page_config(
    page_title="Basic GenAI App",
    page_icon="🤖"
)

st.title("🤖 Basic GenAI App")

prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Generative AI in simple words..."
)


if st.button("Generate"):

    if not prompt.strip():
        st.warning("Please enter a prompt.")
        st.stop()

    backend_url = os.getenv("BACKEND_URL")

    try:
        response = requests.post(
            f"{backend_url}/generate",
            json={
                "prompt": prompt
            },
            timeout=60
        )

        response.raise_for_status()

        result = response.json()

        st.subheader("AI Response")
        st.write(result["answer"])

    except requests.exceptions.RequestException as e:
        st.error(f"Backend connection error: {e}")