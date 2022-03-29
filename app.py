from flask import Flask, request

app = Flask(__name__)

developer_url = "http://127.0.0.1:5000/"


@app.route("/", methods=["GET"])
def home():
    if request.url_root:
        return "alive"
    else:
        return "on development server"


@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "GET":
        return """
        The expected input is a JSON with the following formatting: 
        {
        "data": {
        "area": int,
        "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
        "rooms-number": int,
        "zip-code": int,
        "land-area": Optional[int],
        "garden": Optional[bool],
        "garden-area": Optional[int],
        "equipped-kitchen": Optional[bool],
        "full-address": Optional[str],
        "swimming-pool": Optional[bool],
        "furnished": Optional[bool],
        "open-fire": Optional[bool],
        "terrace": Optional[bool],
        "terrace-area": Optional[int],
        "facades-number": Optional[int],
        "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
        }
        }
"""

    if request.method == "POST":
        content_type = request.headers.get('Content-Type')
        if content_type == "application/json":
            json = request.json
            return json
        else:
            return "Input should be in JSON format. Go to /predict page to learn more about specifics."

        house_data = {
            # TODO: Input structure & matching description in GET request.method
        }
        missing_fields = {k for k, v in house_data.items() if len(v) == 0}
        required_field = {
            # TODO: determine obliged fields
        }
        if not missing_fields:
            try:
                # TODO: convert fields expected to be integers into integers
            except ValueError:
                return {"Error": "Expected numbers for {field_name_here}"}
        else:




if __name__ == "__main__":
    app.run(debug=True)
