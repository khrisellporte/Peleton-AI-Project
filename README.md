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

## Project Structure

```plaintext
.
├── main.py                 # The FastAPI application backend
├── index.html              # The frontend HTML file
├── README.md               # This README file
├── requirements.txt        # Python packages required for the project
├── static                  # Directory for static assets (CSS, images, etc.)
│   └── style.css           # Custom CSS file
└── templates               # Directory for HTML templates (if using Jinja2 with FastAPI)


