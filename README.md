# Emotion Detector AI Web Application

## Project Description
This project is a web-based application developed as part of a software engineering task. The application utilizes **IBM Watson's Natural Language Processing (NLP)** library to analyze text provided by the user and detect various emotions, including anger, disgust, fear, joy, and sadness. 

The backend is built using **Python** and **Flask**, and it features a RESTful API integration to process data and return the results in a formatted response, identifying the "dominant emotion."

## Key Features
* **AI-Powered Analysis:** Uses Watson NLP `EmotionPredict` for high accuracy.
* **RESTful API:** A dedicated endpoint for processing string inputs.
* **Error Handling:** Robust handling for empty inputs and server errors (Status Code 400).
* **Unit Testing:** Integrated Python unit tests to ensure logic reliability.
* **Static Code Analysis:** Clean code following PEP8 standards, verified via Pylint.

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install flask requests`.
3. Run the application: `python3 server.py`.
4. Access the application via `localhost:5000`.

## Author
Sajee
