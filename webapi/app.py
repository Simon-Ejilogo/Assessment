
from flask import Flask, jsonify, request
import psutil
import json
app = Flask(__name__)

@app.route('/system-info', methods=['GET'])
def get_system_info():
    average_load = psutil.getloadavg()[0]
    disk_usage = psutil.disk_usage('/')
    available_disk_space = disk_usage.free

    data = {
        'average_load': average_load,
        'available_disk_space': available_disk_space
    }

    return jsonify(data)

@app.route('/tech-assess', methods=['GET'])
def get_return_value():
    with open('tech_assess.json') as file:
        data = json.load(file)

    return jsonify(data['return_value'])

@app.route('/tech-assess', methods=['POST'])
def update_return_value():
    data = request.get_json()
    new_return_value = data['return_value']

    with open('tech_assess.json', 'w') as file:
        json.dump({'return_value': new_return_value}, file)

    return jsonify({'message': 'Return value updated successfully'})

if __name__ == '__main__':
    app.run()
