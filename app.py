from flask import Flask, request, jsonify
import os
import preprocessing.cleaning_data

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """
    base function that indicates if the web-app is responding or not
    """
    if request.url_root:
        return "alive"
    else:
        return "Something went wrong."


@app.route("/predict", methods=["POST", "GET"])
def predict():
    """
    Core function of the web-app
    :GET: will return expected JSON schema for the ["POST"] method
    :POST: will check the user input before sending it to the preprocessing function
    """

    if request.method == "GET":
        return """
        The expected input should be in the following JSON schema: 
        {
        "data": {
        "area": int,
        "property-type": 'apartment' | 'bungalow' | 'chalet' | 'duplex' | 'ground-floor' | 'loft' | 
        'mansion' | 'master-house' | 'mixed-building' | 'penthouse' | 'residence' | 'studio' | 'triplex' | 
        'villa'[str],
        "bedrooms-number": int,
        "zip-code": int,
        "garden-area": Optional[int],
        "kitchen": Optional['Not equipped' | 'Partially equipped' | 'Fully equipped' | 'Super equipped'][str],
        "balcony": Optional[bool], 
        "terrace-area": Optional[int],
        "facades-number": Optional[int],
        "building-state": Optional['To be renovated' | 'Normal' | 'Excellent' | 'Fully renovated' | 'New'][str]
        "garage": Optional[bool], 
        }
        }
        """

    # checks if the input is in JSON
    if request.method == "POST":
        content_type = request.headers.get('Content-Type')
        if content_type == "application/json":
            user_input = request.json

            # creates lists based on requirements and fills them with missing/wrong typed keys
            required_keys = ["area", "property-type", "bedrooms-number", "zip-code"]
            integer_values = ["area", "bedrooms-number", "zip-code", "garden-area", "terrace_area", "facades_number"]
            boolean_values = ["balcony", "garage"]
            missing_keys = [k for k, v in user_input["data"].items() if not v and k in required_keys]
            should_be_integers = [k for k, v in user_input["data"].items() if not isinstance(v, int)
                                  and k in integer_values]
            should_be_booleans = [k for k, v in user_input["data"].items() if not isinstance(v, bool)
                                  and k in boolean_values]

            # checks if the previous lists are empty, otherwise returns corresponding error message
            if missing_keys:
                return jsonify({"Error": f"Missing required data in following field(s): {missing_keys}."})
            elif should_be_integers:
                return jsonify({"Error": f"Please enter an integer in following field(s): {should_be_integers}"})
            elif should_be_booleans:
                return jsonify({"Error": f"Please enter True or False in following field(s): {should_be_booleans}"})
            else:
                # sends the user_input to the preprocessing function
                return preprocessing.cleaning_data.preprocess(user_input)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
