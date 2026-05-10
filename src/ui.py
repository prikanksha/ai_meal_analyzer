import streamlit as st

def render_analysis_result(result: dict) -> None:
  st.subheader("Meal Summary")
  st.write(result["meal_summary"])

  total = result["total"]

  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Calories", total["calories"])
  col2.metric("Protein (g)", f'{total["protein_g"]:.2f}g')
  col3.metric("Carbs (g)", f'{total["carbs_g"]:.2f}g')
  col4.metric("Fats (g)", f'{total["fat_g"]:.2f}g')

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