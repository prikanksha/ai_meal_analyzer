from typing import List, Literal

from pydantic import BaseModel, Field, AliasChoices

class FoodItem(BaseModel):
  name: str
  estimated_quantity: str | int | float = ""
  calories: float = 0
  protein_g: float = 0
  carbs_g: float = 0
  fat_g: float = 0
  fiber_g: float = 0


class NutritionTotals(BaseModel):
  calories: float = 0
  protein_g: float = 0
  carbs_g: float = 0
  fat_g: float = 0
  fiber_g: float = 0


class MealAnalysis(BaseModel):
  meal_summary: str
  detected_foods: List[FoodItem] = Field(
    default_factory=list,
    validation_alias=AliasChoices("detected_foods", "detected_food_items")
  )
  total: NutritionTotals
  confidence: Literal["low", "medium", "high"] = "low"
  notes: List[str] = Field(default_factory=list)
  improvement_tips: List[str] = Field(default_factory=list)