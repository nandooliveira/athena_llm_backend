# Use an official Node.js runtime as the base image
FROM node:19

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (if available) to the container
COPY package*.json ./

# Install the application's dependencies inside the container
RUN npm install

# Copy the application code to the container
COPY . .

# Build the application if necessary (uncomment if you have a build step)
# RUN npm run build

# Specify the command to run when the container starts
CMD ["npm", "start"]