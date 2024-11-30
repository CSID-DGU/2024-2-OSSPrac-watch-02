# Step 1: Use the official Python image as the base
FROM python:3.10-slim

# Step 2: Set a working directory
WORKDIR /app

# Step 3: Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the rest of the application files
COPY . . 

# Step 5: Expose the port Flask will run on (80 for this example)
EXPOSE 80

# Step 6: Run the Flask application on 0.0.0.0:80
CMD ["python", "team.py"]
