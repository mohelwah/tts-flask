FROM ubuntu

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . app.py /app/
RUN apt update
RUN apt install python3-pip -y
# Install packages from requirements.txt
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python3", "-m", "flask","run", "--host=0.0.0.0"]