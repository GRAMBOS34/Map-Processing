"""
Web server hosted on the Raspberry Pi to send and receive data to and from the laptop
only within the same network
"""

from flask import Flask, request, jsonify
import json
from dependencies import instructionSend

app = Flask(__name__, template_folder="template")

# POST methods mean that data can be sent from the client
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
    
@app.route('/telemetry', methods=['POST'])
def get_telemetry():
    data = request.get_json()

    if data and 'Telemetry' in data:
        array = data['Telemetry']

        print(array) #! temporary

        return jsonify({"status": "success", "message": "Array saved successfully"})
    else:
        return jsonify({"status": "error", "message": "No array provided"}), 400

current_index = 0

# GET methods mean that we can send data to the client
@app.route('/instruct', methods=["GET"])
def send_instructions():
    # Instructions will be (new heading, travel distance in mm, is_end)
    # because i want it to go turn -> forward
    global current_index

    newInstruction = instructionSend.next_point(current_index)
    current_index += 1

    if newInstruction[2] == 0:
        current_index == 0

    return {"instruction": newInstruction}, 200

if __name__ == '__main__':
    # did this so that it can run on localhost:8080
    app.run(host="0.0.0.0", port=8080, debug=True)