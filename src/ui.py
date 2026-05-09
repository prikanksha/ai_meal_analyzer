import streamlit as st

def render_analysis_result(result: dict) -> None:
  st.subheader("Meal Summary")
  st.write(result["meal_summary"])

  total = result["total"]

  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Calories", total["calories"])
  col2.metric("Protein (g)", total["protein_g"])
  col3.metric("Carbs (g)", total["carbs_g"])
  col4.metric("Fats (g)", total["fats_g"])

  st.subheader("Detected Foods")
  st.table(result["detected_foods"])

  st.subheader("Confidence Level")
  st.write(result["confidence"])

  st.subheader("Notes")
  for note in result["notes"]:
    st.write(f"- {note}")

  st.subheader("Improvement Tips")
  for tip in result["improvement_tips"]:
    st.write(f"- {tip}")