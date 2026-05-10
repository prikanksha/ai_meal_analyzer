import pandas as pd

def meals_to_dataframe(meals: list[dict]) -> pd.DataFrame:
  rows = []
  for meal in meals:
    result = meal["result"]
    total = result["total"]

    rows.append({
      "timestamp": meal["timestamp"],
      "meal_summary": result["meal_summary"],
      "calories": total["calories"],
      "protein_g": total["protein_g"],
      "carbs_g": total["carbs_g"],
      "fat_g": total["fat_g"]
    })
  return pd.DataFrame(rows)