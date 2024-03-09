# Python
FROM python:3.8

# Working dir
WORKDIR /app

# Copy current dir contents into the container at /app
COPY . /app

# Install required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available
EXPOSE 5000

# Define env variable
ENV NAME World

# Run app.py when container launches
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
