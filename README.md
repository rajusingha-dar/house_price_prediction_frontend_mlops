House Price Prediction - Frontend
This repository contains the frontend application for the End-to-End House Price Prediction project. It provides a clean, user-friendly interface for interacting with the machine learning backend API.

The application is built using FastAPI to serve a static HTML page, which then uses JavaScript to make live prediction requests to the deployed backend service on Google Cloud.

Features
Interactive Form: A simple and intuitive form for users to input key features of a house.

Dynamic Predictions: Communicates in real-time with the backend ML model to fetch and display price predictions.

Responsive Design: A clean, modern, dark-themed UI that works on both desktop and mobile devices.

Decoupled Architecture: Built as a standalone service that can be developed and deployed independently of the backend.

Tech Stack
Web Framework: Python, FastAPI

Templating: Jinja2

Frontend: HTML, JavaScript, Tailwind CSS

Deployment: Docker, Google Cloud Run

Local Setup and Installation
Follow these steps to run the frontend application on your local machine.

1. Prerequisites

Python 3.8+ installed.

The backend API must be running (either locally on http://127.0.0.1:8000 or deployed to the cloud).

2. Clone the Repository (if applicable)

git clone https://github.com/rajusingha-dar/house_price_prediction_frontend_mlops.git
cd house_price_prediction_frontend_mlops

3. Create and Activate a Virtual Environment

# Create the environment
python -m venv venv

# Activate it (macOS/Linux)
source venv/bin/activate

# Activate it (Windows)
.\venv\Scripts\activate

4. Install Dependencies
Install the required Python libraries.

pip install -r requirements.txt

5. Configure Environment Variables
Create a .env file in the root of the project by copying the example file:

# For Windows
copy .env.example .env

# For macOS/Linux
cp .env.example .env

Open the .env file and ensure the BACKEND_API_URL is pointing to your running backend server (e.g., http://127.0.0.1:8000 for local testing or the live Cloud Run URL).

6. Run the FastAPI Server Locally
Start the local web server. We recommend running it on a different port than the backend, such as 8001.

uvicorn app.main:app --reload --port 8001

The application will be available at http://127.0.0.1:8001.

Deployment to Google Cloud
This project is configured for automated deployment to Google Cloud Run via the CI/CD pipeline defined in .github/workflows/main.yml.

The pipeline triggers on every push to the main (or master) branch and will:

Build a Docker container for the frontend application.

Push the container to Google Artifact Registry.

Deploy the container as a new service to Cloud Run.

During deployment, the BACKEND_API_URL environment variable is set in the Cloud Run service to point to the live backend API, ensuring the deployed frontend communicates with the deployed backend.