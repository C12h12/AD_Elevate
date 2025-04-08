# ✅ MUST BE FIRST Streamlit command
import streamlit as st

# 📦 Other imports
from textblob import TextBlob
import requests
from pages.navbar import render_navbar

def enhance_func():
    # 📌 Optional: Render navbar (after set_page_config)
    render_navbar()

# 🔐 Together AI API Setup
    TOGETHER_API_KEY = "f3532b6c8602b015077d5c0dd7b6480fd433a29a569094ff44e947bbeb02a929"
    API_URL = "https://api.together.xyz/v1/completions"
    MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"

# 🎯 Rewrite function
    def improve_campaign_text(original_text, tone):
        prompt = f"""
    You are a top-tier social media marketing expert who deeply understands current trends, audience psychology, and platform-specific engagement strategies.

    Your goal is to transform the input into a captivating, interactive, and conversion-driven campaign text. The output should align with the original sentiment — being funny, professional, tempting, or witty as needed — and significantly outperform the original in terms of appeal and effectiveness.

    Rewrite the following marketing text in a *{tone.lower()}* tone to make it more engaging, persuasive, and tailored for high-performing social media content.

    Original Text:
    \"{original_text}\"

    Improved Version:
        """

        headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
        }

        payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "max_tokens": 200,
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 0.9,
        "repetition_penalty": 1.1
    }

        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            text = result.get("choices", [{}])[0].get("text", "").strip()
            return text if text else "[No output returned 🤔]"
        else:
            return f"[ERROR] {response.status_code}: {response.text}"

# 😊 Sentiment
    def get_sentiment(text):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0.2:
            return "😊 Positive"
        elif polarity < -0.2:
            return "😠 Negative"
        else:
            return "😐 Neutral"

# 📊 Prediction mock
    def predict_success(text):
        sentiment = TextBlob(text).sentiment.polarity
        length_score = len(text)
        prediction = (length_score > 60 and sentiment > 0.2)
        return "✅ Likely to Succeed" if prediction else "❌ Unlikely to Succeed"

# 🌟 Streamlit UI
    user_input = st.text_area("Enter your campaign text", height=150)
    tone = st.selectbox("Choose the tone", ["Exciting", "Professional", "Funny", "Friendly", "Urgent"])

    if st.button("✨ Improve and Analyze"):
        with st.spinner("Working on it..."):
            improved = improve_campaign_text(user_input, tone)
            sentiment = get_sentiment(improved)
            prediction = predict_success(improved)

            st.markdown("### 📝 Improved Campaign Text")
            st.success(improved)

            st.markdown("### 💬 Sentiment")
            st.info(sentiment)

            st.markdown("### 📊 Predicted Success")
            st.warning(prediction)


