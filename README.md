# Test Management System

## Project Description

This project is an online test management system built with FastAPI and MySQL.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/test_management_system.git
   cd test_management_system
2. Install dependencies:
    ```bash
   pip install -r requirements.txt
3. Set up the database:
    ````
    Make sure MySQL is running and update the DATABASE_URL in app/database.py
4. Run the application:
   ```bash
   uvicorn app.main:app --reload

## Docker
1. Build the Docker image:
   ```bash
   docker build -t test_management_system .
2. Run the Docker container:
   ```bash
   docker run -d --name test_management_system -p 8000:8000 test_management_system
