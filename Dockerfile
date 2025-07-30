FROM python:3.13.5

# Set the working directory in the container
WORKDIR /app

# Copy the  requirements file into the container
COPY  requirements.txt .
# Install dependencies
RUN pip install -r requirements.txt 

# Copy the rest of the application code into the container
COPY . .  

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]

