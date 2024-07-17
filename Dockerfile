# Use the official Python base image
FROM python:3.10.14-slim

# Set the working directory inside the container
WORKDIR /

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 3000

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app","--reload", "--host", "0.0.0.0", "--port", "3000"]
