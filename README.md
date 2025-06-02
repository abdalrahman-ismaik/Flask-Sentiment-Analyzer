# Sentiment Analysis Web Application

A modern web application that performs sentiment analysis on text using TextBlob's Natural Language Processing capabilities. The application provides real-time sentiment analysis with a sleek, dark-themed user interface.

## Practice Project Overview

This project demonstrates the integration of Natural Language Processing using TextBlob into a web application. The application performs sentiment analysis on provided text and is deployed using the Flask framework.

### Learning Objectives
Through this project, you will:
- Work with Natural Language Processing libraries
- Create an AI-powered web application
- Deploy applications using Flask framework
- Implement error handling and testing
- Practice code quality standards

### Project Tasks
1. Clone the project repository
2. Create a sentiment analysis application using TextBlob
3. Format the output of the application
4. Package the application
5. Run Unit tests on your application
6. Deploy as web application using Flask
7. Incorporate error handling
8. Run static code analysis

## Features

- Real-time sentiment analysis using TextBlob
- Modern dark blue UI theme
- Responsive design
- Error handling
- RESTful API endpoint

## Technologies Used

- Python 3.x
- Flask
- TextBlob for NLP
- HTML5/CSS3
- JavaScript
- Bootstrap 5

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python server.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
├── server.py                # Main Flask application
├── requirements.txt         # Project dependencies
├── SentimentAnalysis/      # Sentiment analysis module
│   ├── __init__.py
│   └── sentiment_analysis.py
├── static/                 # Static files
│   └── mywebscript.js
└── templates/             # HTML templates
    ├── index.html
    └── error.html
```

## API Usage

Send a GET request to `/sentimentAnalyzer` with the `textToAnalyze` parameter:
```
GET /sentimentAnalyzer?textToAnalyze=Your text here
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
