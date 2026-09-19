import streamlit as st
import requests


# Page configuration
st.set_page_config(
    page_title="Basic GenAI App",
    page_icon="🤖",
    layout="centered"
)


# Title
st.title("🤖 Basic GenAI App")

st.write("Streamlit → FastAPI → OpenAI")


# User input
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Generative AI in simple words..."
)


# Generate button
if st.button("Generate", type="primary"):

    if not prompt.strip():

        st.warning("Please enter a prompt.")

    else:

        try:

            response = requests.post(
                "http://backend:8000/generate",
                json={
                    "prompt": prompt
                },
                timeout=60
            )

            if response.status_code == 200:

                result = response.json()

                st.subheader("AI Response")

                st.write(result["answer"])

            else:

                st.error(
                    f"Backend error: {response.status_code}"
                )

        except requests.exceptions.RequestException as e:

            st.error(
                f"Could not connect to backend: {e}"
            )