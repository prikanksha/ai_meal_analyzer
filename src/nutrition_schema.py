from typing import List

from pydantic import BaseModel

class FoodItem(BaseModel):
  name: str
  estimated_quantity: str
  calories: int
  protein_g: int
  carbs_g: int
  fats_g: int
  fiber_g: int

class NutritionTotals(BaseModel):
  calories: int
  protein_g: int
  carbs_g: int
  fats_g: int
  fiber_g: int

class MealAnalysis(BaseModel):
  meal_summary: str
  detected_food_items: List[FoodItem]
  total: NutritionTotals
  confidence: str
  notes: List[str]
  improvement_tips: List[str]