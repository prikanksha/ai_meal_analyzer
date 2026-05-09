# AI Meal Analyzer 🍽️

An AI-powered meal analysis application that estimates calories and macronutrients from meal images using OpenAI vision models.

## Features

- Upload meal photos
- Supports JPG, PNG, HEIC, and HEIF
- AI-powered food detection
- Nutrition estimation
- Structured JSON validation with Pydantic
- Modular architecture
- Error handling and logging

## Tech Stack

- Python
- Streamlit
- OpenAI API
- Pydantic
- Pillow
- pillow-heif

## Project Structure

```text
ai_meal_analyzer/
│
├── app.py
├── requirements.txt
│
└── src/
    ├── ai_client.py
    ├── image_utils.py
    ├── nutrition_schema.py
    ├── prompts.py
    ├── logger.py
    └── ui.py