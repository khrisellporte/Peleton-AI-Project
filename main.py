from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Hugging Face sentiment analysis pipeline
classifier = pipeline('sentiment-analysis')

# Load GPT-2 model for generating AI recommendations
recommendation_model = pipeline("text-generation", model="gpt2")

# Pydantic models for request and response bodies
class User(BaseModel):
    username: str
    goals: List[str]
    fitness_level: str

class WorkoutRecommendation(BaseModel):
    workout_name: str
    workout_type: str
    duration_minutes: int
    intensity: str

class ClassificationRequest(BaseModel):
    user_input: str

class ClassificationResponse(BaseModel):
    explanation: str

class RecommendationResponse(BaseModel):
    username: str
    recommendations: List[WorkoutRecommendation]
    ai_recommendation: str

# Sample workout data
workout_data: Dict[str, Dict[str, WorkoutRecommendation]] = {
    "strength": {
        "beginner": WorkoutRecommendation(workout_name="Beginner Strength Training", workout_type="Strength", duration_minutes=20, intensity="low"),
        "intermediate": WorkoutRecommendation(workout_name="Intermediate Strength Training", workout_type="Strength", duration_minutes=30, intensity="medium"),
        "advanced": WorkoutRecommendation(workout_name="Advanced Strength Training", workout_type="Strength", duration_minutes=40, intensity="high"),
    },
    "cardio": {
        "beginner": WorkoutRecommendation(workout_name="Beginner Cardio Session", workout_type="Cardio", duration_minutes=15, intensity="low"),
        "intermediate": WorkoutRecommendation(workout_name="Intermediate Cardio Session", workout_type="Cardio", duration_minutes=25, intensity="medium"),
        "advanced": WorkoutRecommendation(workout_name="Advanced Cardio Session", workout_type="Cardio", duration_minutes=35, intensity="high"),
    },
    "flexibility": {
        "beginner": WorkoutRecommendation(workout_name="Beginner Yoga Flow", workout_type="Flexibility", duration_minutes=25, intensity="low"),
        "intermediate": WorkoutRecommendation(workout_name="Intermediate Yoga Flow", workout_type="Flexibility", duration_minutes=35, intensity="medium"),
        "advanced": WorkoutRecommendation(workout_name="Advanced Yoga Flow", workout_type="Flexibility", duration_minutes=45, intensity="high"),
    },
}

# Sample Peloton product data
peloton_products = [
    {"name": "Peloton Bike", "description": "A high-tech indoor bike designed for cardio and strength training."},
    {"name": "Peloton Tread", "description": "A treadmill built for running, walking, and total body workouts."},
    {"name": "Peloton Guide", "description": "An AI-powered guide to strength training that adapts to your form."},
    {"name": "Peloton App", "description": "A digital platform offering thousands of live and on-demand classes."},
    {"name": "Peloton Bike+", "description": "An upgraded version of the Peloton Bike with additional features."},
    {"name": "Peloton Heart Rate Band", "description": "A heart rate monitor that helps you track your workout intensity."},
    {"name": "Peloton Weights", "description": "A set of dumbbells designed for strength training at home."},
    {"name": "Peloton Yoga Mat", "description": "A high-quality mat for yoga, stretching, and floor exercises."}
]

@app.post("/recommendation/", response_model=RecommendationResponse)
def get_workout_recommendation(user: User) -> RecommendationResponse:
    # Generate predefined workout recommendations
    recommendations = []
    for goal in user.goals:
        if goal in workout_data:
            recommendation = workout_data[goal].get(user.fitness_level)
            if recommendation:
                recommendations.append(recommendation)

    if not recommendations:
        recommendations.append(WorkoutRecommendation(workout_name="General Fitness", workout_type="Mixed", duration_minutes=30, intensity="medium"))

    # Generate AI recommendation for a Peloton product
    prompt = f"Suggest a Peloton product for a user who is {user.fitness_level} level and wants to focus on {', '.join(user.goals)}."
    ai_recommendation_response = recommendation_model(prompt, max_length=50, num_return_sequences=1)[0]
    ai_recommendation_text = ai_recommendation_response['generated_text'].strip()

    # Select a Peloton product from the list based on user input (simplified logic)
    selected_product = peloton_products[0]  # Simplified selection for example purposes

    ai_recommendation = f"We recommend the {selected_product['name']}: {selected_product['description']}"

    return RecommendationResponse(
        username=user.username,
        recommendations=recommendations,
        ai_recommendation=ai_recommendation
    )

@app.post("/classify/", response_model=ClassificationResponse)
def classify_text(request: ClassificationRequest) -> ClassificationResponse:
    result = classifier(request.user_input)[0]
    sentiment = result['label']
    confidence = round(result['score'] * 100, 2)

    if sentiment == "NEGATIVE":
        explanation = f"It seems like you're feeling a bit down. We detected a negative sentiment with {confidence}% confidence. We're here to help!"
    elif sentiment == "POSITIVE":
        explanation = f"You're in a great mood! We detected a positive sentiment with {confidence}% confidence. Keep up the good energy!"
    else:
        explanation = f"Your message seems neutral. We detected this sentiment with {confidence}% confidence. Let's keep going!"

    return ClassificationResponse(explanation=explanation)
