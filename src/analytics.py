import pandas as pd

def meals_to_dataframe(meals: list[dict]) -> pd.DataFrame:
  rows = []

  for meal in meals:
    result = meal["result"]
    total = result["total"]

    rows.append({
      "timestamp": meal["timestamp"],
      "meal_summary": result["meal_summary"],
      "calories": total.get("calories", 0),
      "protein_g": total.get("protein_g", 0),
      "carbs_g": total.get("carbs_g", 0),
      "fat_g": total.get("fat_g", 0),
      "fiber_g": total.get("fiber_g", 0),
    })
  df = pd.DataFrame(rows)

  if not df.empty:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.sort_values("timestamp", inplace=True)

  return df