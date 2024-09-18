# Dockerfile for Django with Gunicorn and PostgreSQL

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client
    
RUN apt-get update && apt-get install -y libpq-dev

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt /code/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Copy the rest of the application code
COPY . /code/

RUN python manage.py collectstatic --noinput

# Expose port 8000 (Gunicorn will serve on this port)
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]

