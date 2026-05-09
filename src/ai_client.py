import json
import os
import time

from dotenv import load_dotenv
from openai import OpenAI

from src.image_utils import image_to_base64
from src.prompts import MEAL_ANALYSIS_PROMPT
from src.nutrition_schema import MealAnalysis
from src.logger import logger

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_meal(uploaded_file):
  start_time = time.time()
  logger.info("Starting meal analysis")
  image_data = image_to_base64(uploaded_file)

  logger.info("Sending image to OpenAI API for analysis")
  response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
      {
        "role": "user",
        "content": [
          {"type": "input_text", "text": MEAL_ANALYSIS_PROMPT},
          {
            "type": "input_image",
            "image_url": f"data:image/jpeg;base64,{image_data}",
          },
        ],
      }
    ],
  )

  logger.info("Received response from OpenAI API")
  parsed_response = json.loads(response.output_text)

  validated_response = MealAnalysis(**parsed_response)
  logger.info("Successfully validated AI response")
  elapsed_time = time.time() - start_time
  logger.info(f"Meal analysis completed in {elapsed_time:.2f} seconds")
  return validated_response