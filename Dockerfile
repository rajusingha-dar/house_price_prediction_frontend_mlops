# Start with an official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code into the container
COPY ./app /app/app
COPY ./templates /app/templates

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application using uvicorn
# Uses the $PORT environment variable provided by Cloud Run
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
