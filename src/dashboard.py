import plotly.express as px
import streamlit as st

def render_dashboard(df):
  st.subheader("Nutrition Dashboard")

  if df.empty:
    st.info("No meal data available.")
    return

  col1, col2, col3 = st.columns(3)

  col1.metric("Average Calories", f"{round(df['calories'].mean(), 1)}")
  col2.metric("Average Protein (g)", f"{round(df['protein_g'].mean(), 1)}")
  col3.metric("Meals Logged", f"{len(df)}")

  calorie_chart = px.line(df, x="timestamp", y="calories", title="Calories Trend", markers=True)
  protein_chart = px.line(df, x="timestamp", y="protein_g", title="Protein Trend", markers=True)

  st.plotly_chart(calorie_chart, use_container_width=True)
  st.plotly_chart(protein_chart, use_container_width=True)