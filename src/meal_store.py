import json
from datetime import datetime
from pathlib import Path

DATA_DIR = Path("data")
MEALS_FILE = DATA_DIR / "meals.json"

def save_meal(result: dict) -> None:
  DATA_DIR.mkdir(exist_ok=True)

  meals = load_meals()

  meal_record = {
    "timestamp": datetime.now().isoformat(timespec="seconds"),
    "result": result,
  }

  meals.append(meal_record)
  with open(MEALS_FILE, "w") as file:
    json.dump(meals, file, indent=2)

def load_meals() -> list[dict]:
  if not MEALS_FILE.exists():
    return []

  with open(MEALS_FILE, "r") as file:
    return json.load(file)