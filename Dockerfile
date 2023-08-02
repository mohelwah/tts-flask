FROM python:3.9-slim

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . app.py /app/
RUN apt update


RUN pip install -r requirements.txt
EXPOSE 8080
CMD python app.py