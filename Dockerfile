# Use an official Ubuntu base image
FROM ubuntu:jammy

# Set the working directory in the container
WORKDIR /app

# Update and install necessary packages
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y unixodbc unixodbc-dev

# Copy the application code
COPY . /app/

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000
EXPOSE 1433


CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8000"]