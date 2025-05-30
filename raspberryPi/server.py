"""
Web server hosted on the Raspberry Pi to send and receive data to and from the laptop
only within the same network
"""

from flask import Flask, request, jsonify
import json

app = Flask(__name__, template_folder="template")

@app.route('/new_coords', methods=['POST'])
def save_array():
    # Get the array from the request
    data = request.get_json()
    
    if data and 'coordinates' in data:
        array = data['coordinates']
        
        # Save the array to a file (or process it as needed)
        with open('coordinates.json', 'w') as f:
            json.dump(array, f)
        
        return jsonify({"status": "success", "message": "Array saved successfully"})
    else:
        return jsonify({"status": "error", "message": "No array provided"}), 400
    

if __name__ == '__main__':
    # did this so that it can run on localhost:8080
    app.run(host="0.0.0.0", port=8080, debug=True)