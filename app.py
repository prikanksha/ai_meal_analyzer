
import json
import streamlit as st

from src.ai_client import analyze_meal
from src.ui import render_analysis_result
from pydantic import ValidationError

st.set_page_config(page_title="AI Meal Analyzer", page_icon="🍽️", layout="centered")

st.title("🍽️ AI Meal Analyzer")
st.write("Upload a photo of your meal and get an estimated nutritional breakdown.")

uploaded_file = st.file_uploader("Upload your meal photo", type=["jpg", "jpeg", "png", "heif", "heic"])

if uploaded_file:
  st.image(uploaded_file, caption="Uploaded Meal Photo", use_container_width=True)

  if st.button("Analyze Meal"):
    with st.spinner("Analyzing meal..."):
      try:
        result = analyze_meal(uploaded_file)
        render_analysis_result(result)
      except ValidationError as e:
        st.error("AI response format was invalid.")
        st.exception(e)
      except json.JSONDecodeError as e:
        st.error("Failed to parse AI response.")
        st.exception(e)
      except Exception as e:
        st.error("Unexpected error occurred.")
        st.exception(e)