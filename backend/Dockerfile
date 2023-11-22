# Use Python 3.10 image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install OS dependencies
RUN apt update -y
RUN apt install -y gcc python3-dev

# Install dependencies from requirements.txt
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir gunicorn

# Add the current directory to Docker image
COPY . .

# Run the application
ENV FLASK_APP=app
CMD ["flask", "--app", "app", "run", "-h", "0.0.0.0"]
