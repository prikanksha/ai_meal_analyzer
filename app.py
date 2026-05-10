
import json
import streamlit as st
from pydantic import ValidationError

from src.ai_client import analyze_meal
from src.ui import render_analysis_result
from src.meal_store import save_meal, load_meals
from src.analytics import meals_to_dataframe
from src.dashboard import render_dashboard

st.set_page_config(page_title="AI Meal Analyzer", page_icon="🍽️", layout="centered")

st.title("🍽️ AI Meal Analyzer")
st.write("Upload a photo of your meal and get an estimated nutritional breakdown.")

if "latest_result" not in st.session_state:
  st.session_state.latest_result = None

uploaded_file = st.file_uploader("Upload your meal photo", type=["jpg", "jpeg", "png", "heif", "heic"])

if uploaded_file:
  st.image(uploaded_file, caption="Uploaded Meal Photo", use_container_width=True)

  if st.button("Analyze Meal"):
    with st.spinner("Analyzing meal..."):
      try:
        result = analyze_meal(uploaded_file)
        st.session_state.latest_result = result
      except ValidationError as e:
        st.error("AI response format was invalid.")
        st.exception(e)
      except json.JSONDecodeError as e:
        st.error("Failed to parse AI response.")
        st.exception(e)
      except Exception as e:
        st.error("Unexpected error occurred.")
        st.exception(e)

if st.session_state.latest_result is not None:
  render_analysis_result(st.session_state.latest_result)
  if st.button("Save Meal"):
    save_meal(st.session_state.latest_result)
    st.success("Meal saved successfully!")

st.divider()
st.subheader("Meal History")

meals = load_meals()

if not meals:
  st.info("No saved meals yet.")
else:
  for meal in reversed(meals[-5:]):
    result = meal["result"]
    total = result["total"]

    with st.expander(f'{meal["timestamp"]} — {result["meal_summary"]}'):
      st.write(f'Calories: {total["calories"]}')
      st.write(f'Protein: {total["protein_g"]}g')
      st.write(f'Carbs: {total["carbs_g"]}g')
      st.write(f'Fat: {total["fat_g"]}g')

st.divider()

df = meals_to_dataframe(meals)
render_dashboard(df)
