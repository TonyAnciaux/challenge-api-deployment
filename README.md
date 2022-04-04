# Elisa-API 

## Description 

Web application used to predict prices of real-estate in Belgium based on historical data. 

## Installation 

This application doesn't require any installation process and works exclusively through API.
All the necessary libraries and dependencies to make it work are self-contained. 
It only needs a valid internet connection and a software that allows for API requests such as Postman. 

## Usage

### Available Routes 

#### Main Route
https://pumpkin-pie-15657.herokuapp.com is the main route of the API. 
It only takes **["GET"]** request and returns the state of the web-app. 
- If *"alive"*, the return indicates the web-app is ready for an API request. 
- If *"Something went wrong."*, the return indicates the web-app is not ready or disfonctionning. 

#### Prediction Route
https://pumpkin-pie-15657.herokuapp.com/predict takes **["GET"]** and **["POST"]** requests.
If **["GET"]**, will return the expected schema of the JSON request. 
When sending a valid JSON through **["POST"]** request, the web-app will return a prediction price. 

### Expected Format 

You can access https://pumpkin-pie-15657.herokuapp.com/predict through **["GET"]** method for specific schema structure.

#### The mandatory fields are the following: 
- area **[int]**
- property-type **[str]**: 'apartment' | 'bungalow' | 'chalet' | 'duplex' | 'ground-floor' | 'loft' | 'mansion' | 'master-house' | 'mixed-building' | 'penthouse' | 'residence' | 'studio' | 'triplex' | 'villa'
- bedrooms-number **[int]**
- zip-code **[int]**

If missing or incorrect, an error message will be raised with an indication on the concerned field(s). 

#### Some precisions
If the building/apartment concerned for the prediction doesn't have any **garden** or **terrace**, 
the input for *garden-area* and *terrace-area* fields should be "0". 


## Future developments

- The validation system is to be improved as well as the error handling messages 
- The fine-tuning and correction of the prediction model: at this stage, it  can suffer some imprecisions and sometimes even return negative prices 
