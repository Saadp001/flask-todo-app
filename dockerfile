# 1. Use official Python image
FROM python:3.11

# 2. Work directory inside container
WORKDIR /app

# 3. Copy requirement file
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy everything into container
COPY . .

# 6. Expose Flask port
EXPOSE 5000

# 7. Run the Flask app
CMD ["python", "app.py", "--host=0.0.0.0"]

