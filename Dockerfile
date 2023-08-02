FROM python:3.9-slim

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . app.py /app/
RUN apt update
RUN apt install python3-pip -y
# Install packages from requirements.txt
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
RUN python3 app.py