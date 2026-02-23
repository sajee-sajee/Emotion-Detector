import requests
import json

def emotion_detector(text_to_analyze):
    """
    Function to send text to Watson NLP Emotion Analysis service.
    """
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Custom header required by the API
    header = {"Letters-Id": "watson-emotion-v1-dev"}
    
    # Dictionary object containing the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending a POST request to the API
    response = requests.post(url, json=myobj, headers=header)
    
    # Returning the response text from the API
    return response.text
