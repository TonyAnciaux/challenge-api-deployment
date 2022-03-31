from flask import Flask, request
import preprocessing.cleaning_data

app = Flask(__name__)

developer_url = "http://127.0.0.1:5000/"


@app.route("/", methods=["GET"])
def home():
    if request.url_root:
        return "alive"
    else:
        return "Something went wrong."


@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "GET":
        return """
        The expected input should be in the following JSON format: 
        {
        "data": {
        "area": "MANDATORY [int]",
        "property-type": "MANDATORY ['apartment' | 'bungalow' | 'chalet' | 'duplex' | 'ground-floor' | 'loft' | 
        'mansion' | 'master-house' | 'mixed-building' | 'penthouse' | 'residence' | 'studio' | 'triplex' | 
        'villa' ] [str]",
        "bedrooms-number": "MANDATORY [int]",
        "zip-code": "MANDATORY [int]",
        "garden-area": "OPTIONAL - (leave empty if no garden) [int]",
        "kitchen": "OPTIONAL ['Not equipped' | 'Partially equipped' | 'Fully equipped' | 'Super equipped'] [str]",
        "balcony": "OPTIONAL [bool]", 
        "terrace-area": "OPTIONAL - (leave empty if no terrace) [int]",
        "facades-number": "OPTIONAL [int]",
        "building-state": "OPTIONAL ['To be renovated' | 'Normal' | 'Excellent' | 'Fully renovated' | 'New'] [str]"
        "garage": "OPTIONAL [bool]", 
        }
        }
"""

    if request.method == "POST":
        content_type = request.headers.get('Content-Type')
        if content_type == "application/json":
            user_input = request.json
            required_keys = ["area", "property-type", "bedrooms-number", "zip-code"]
            missing_keys = [k for k, v in user_input.items() if len(v) == 0 and k in required_keys]
            if missing_keys:
                return {"Error": f"Missing data in following required field(s): {missing_keys}."}
            else:
                # TODO: convert expected-integers fields into integers ("try int(field)/ except ValueError" method)
                # try
                # return user_input
                return preprocessing.cleaning_data.preprocess(user_input)
        else:
            return "Input should be in JSON format. Go to /predict for specific details."


"""
        # try:
        # except ValueError:
        #     return {"Error": "Expected numbers for {field_name_here}"}
        
        
        #     house_data = {
        #         # TODO: Input structure & matching description in GET request.method
        #     }
        # 
"""

if __name__ == "__main__":
    app.run(port=5000)
