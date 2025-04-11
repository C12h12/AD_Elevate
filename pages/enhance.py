# ===== Imports =====
import os
import requests
import streamlit as st
from textblob import TextBlob
from dotenv import load_dotenv
from pages.navbar import render_navbar

# ===== Main Enhancement Function =====
def enhance_func():
    # 🔧 Load environment variables
    
    hf_token = os.getenv("HF_TOKEN")
    together_api_key = os.getenv("TOGETHER_API_KEY")  # Optional: Move Together API key to .env too

    if not hf_token:
        load_dotenv()
        hf_token = os.getenv("HF_TOKEN")
        

    if not together_api_key:
        together_api_key = os.getenv("TOGETHER_API_KEY")
        

    # 📌 Optional: Render navbar
    render_navbar()

    # 🔐 Hugging Face API setup
    HF_EMOTION_MODEL_URL = "https://api-inference.huggingface.co/models/bhadresh-savani/bert-base-go-emotion"
    HF_HEADERS = {"Authorization": f"Bearer {hf_token}"}

    # 🔐 Together AI API setup
    TOGETHER_API_URL = "https://api.together.xyz/v1/completions"
    TOGETHER_MODEL = "mistralai/Mistral-7B-Instruct-v0.1"
    TOGETHER_HEADERS = {
        "Authorization": f"Bearer {together_api_key}",
        "Content-Type": "application/json"
    }

    # 🎯 Improve Campaign Text
    def improve_campaign_text(original_text, tone):
        prompt = f"""
You are a top-tier social media marketing expert who deeply understands current trends, audience psychology, and platform-specific engagement strategies.

Your goal is to transform the input into a captivating, interactive, and conversion-driven campaign text. The output should align with the original sentiment — being funny, professional, tempting, or witty as needed — and significantly outperform the original in terms of appeal and effectiveness.

Rewrite the following marketing text in a *{tone.lower()}* tone to make it more engaging, persuasive, and tailored for high-performing social media content.

Original Text:
\"{original_text}\"

Improved Version:
        """

        payload = {
            "model": TOGETHER_MODEL,
            "prompt": prompt,
            "max_tokens": 200,
            "temperature": 0.7,
            "top_k": 50,
            "top_p": 0.9,
            "repetition_penalty": 1.1
        }

        response = requests.post(TOGETHER_API_URL, headers=TOGETHER_HEADERS, json=payload)
        if response.status_code == 200:
            text = response.json().get("choices", [{}])[0].get("text", "").strip()
            return text if text else "[No output returned 🤔]"
        else:
            return f"[ERROR] {response.status_code}: {response.text}"

    # 😊 Sentiment Detection
    def get_sentiment(text):
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.2:
            return "😊 Positive"
        elif polarity < -0.2:
            return "😠 Negative"
        else:
            return "😐 Neutral"

    # 📊 Success Prediction (Mock Logic)
    def predict_success(text):
        sentiment = TextBlob(text).sentiment.polarity
        prediction = (len(text) > 60 and sentiment > 0.2)
        return "✅ Likely to Succeed" if prediction else "❌ Unlikely to Succeed"

    # 💬 Emotion Score Extraction
    def get_emotion_scores(text):
        response = requests.post(HF_EMOTION_MODEL_URL, headers=HF_HEADERS, json={"inputs": text})
        if response.status_code == 200:
            results = response.json()[0]
            top_emotions = sorted(results, key=lambda x: x['score'], reverse=True)[:3]
            return ", ".join([f"{e['label']} ({e['score']:.2f})" for e in top_emotions])
        else:
            return f"[ERROR] Emotion API: {response.status_code} - {response.text}"

    # 🌟 Streamlit UI
    
    user_input = st.text_area("📢 Enter your campaign text", height=150)
    tone = st.selectbox("🎭 Choose the tone", ["Exciting", "Professional", "Funny", "Friendly", "Urgent"])

    if st.button("✨ Improve and Analyze"):
        with st.spinner("Working on it..."):
            improved = improve_campaign_text(user_input, tone)
            sentiment = get_sentiment(improved)
            prediction = predict_success(improved)
            emotion_scores = get_emotion_scores(improved)

            st.markdown("### 🎯 Improved Campaign Text")
            st.success(improved)

            st.markdown("###  Sentiment")
            st.info(sentiment)
            st.markdown("###  Predicted Success")
            st.warning(prediction)

           
