# Use a NodeJS base image
FROM node:18

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the working directory
COPY . .

# Install the application dependencies
RUN npm install

# Expose port 8080 for communication
EXPOSE 8080

# Run the NodeJS application
CMD ["node", "main.js"]
