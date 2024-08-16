# Peloton Workout Recommendations with AI

This project is a simple web application that provides personalized workout recommendations based on user input. It also includes AI-powered sentiment analysis and additional Peloton workout suggestions to enhance the user experience.

## Features

- **User Input:** Users can input their name, fitness goals, and fitness level to receive personalized workout recommendations.
- **Sentiment Analysis:** The application uses AI (powered by Hugging Face) to analyze the user's input and determine the sentiment, providing a personalized message based on the sentiment.
- **AI-Powered Recommendations:** The app also provides additional workout recommendations based on AI analysis of user goals.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** FastAPI (Python)
- **AI/ML:** Hugging Face Transformers for sentiment analysis and text generation using GPT-2
- **Deployment:** Local server using Uvicorn

## Setup and Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Virtual environment tool (`venv`)

### Installation Steps

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/peloton-workout-recommendations.git
    cd peloton-workout-recommendations
    ```

2. **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\\Scripts\\activate`
    ```

3. **Install the Required Packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**
    ```bash
    uvicorn main:app --reload
    ```

5. **Open the Application:**
    - Open your web browser and go to `http://127.0.0.1:8000` to access the application.

API Endpoints
POST /classify/

Description: Analyzes user input and returns sentiment classification.
Request Body:
json
Always show details

Copy code
{
    "user_input": "I want to improve my cardio and strength."
}
Response:
json
Always show details

Copy code
{
    "explanation": "It seems like you're feeling positive. We detected a positive sentiment with 96.45% confidence."
}
POST /recommendation/

Description: Generates personalized workout recommendations and an AI-powered suggestion.
Request Body:
json
Always show details

Copy code
{
    "username": "John",
    "goals": ["strength", "cardio"],
    "fitness_level": "intermediate"
}
Response:
json
Always show details

Copy code
{
    "username": "John",
    "recommendations": [
        {
            "workout_name": "Intermediate Strength Training",
            "workout_type": "Strength",
            "duration_minutes": 30,
            "intensity": "medium"
        },
        {
            "workout_name": "Intermediate Cardio Session",
            "workout_type": "Cardio",
            "duration_minutes": 25,
            "intensity": "medium"
        }
    ],
    "ai_recommendation": "Based on your goals, we recommend trying Peloton's HIIT Cardio program for maximum results!"
}
Contributing
Contributions are welcome! Please open an issue or submit a pull request with any changes.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For any inquiries, please contact yourname@domain.com. """

Saving the README content to a file
file_path = "/mnt/data/README.md" with open(file_path, "w") as file: file.write(readme_content)

file_path
