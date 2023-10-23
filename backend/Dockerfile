# Use Python 3.10 image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install OS dependencies
RUN apt update -y
RUN apt install -y gcc python3-dev

# Install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir gunicorn

# Add the current directory to Docker image
COPY .. .

# Make port 5000 available to the world outside this container
# EXPOSE 8000

# Run the application
ENV FLASK_APP=app
CMD ["python","app.py"]
