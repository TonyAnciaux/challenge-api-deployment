# Elisa-API 

## Description 

Web application that aims to predict price of real-estate in Belgium based on historical prices. 

## Installation 

This application is reachable from any API request and only needs a valid internet connection and 
a software for API requests such as Postman. 

## Usage

### Available Routes 

https://pumpkin-pie-15657.herokuapp.com is the main route. It only takes ["GET"] request and check if the 
network is alive.

https://pumpkin-pie-15657.herokuapp.com/predict takes ["GET"] and ["POST"] requests.
If ["GET"], will return the correct format of the JSON request. 
When sending a valid JSON through ["POST"] request, will return a prediction price. 

### Expected Format 

You can access https://pumpkin-pie-15657.herokuapp.com/predict with no input for specific details.

The mandatory fields are the following: 
- area [int]
- property-type [str]
- bedrooms-number [int]
- zip-code [int]


If missing, an error message will be raised followed by the field missing/wrongly input. 
