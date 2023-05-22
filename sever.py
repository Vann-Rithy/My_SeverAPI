from flask import Flask, jsonify
import os

app = Flask(__name__)

members = [
    {"name": "Vann Rithy", "gender": "Male", "school": "RUPP"},
    {"name": "Samantha Smith", "gender": "Female", "school": "Harvard"},
    {"name": "Samantha Smith", "gender": "Female", "school": "Harvard"},
    {"name": "Samantha Smith", "gender": "Female", "school": "Harvard"},
    {"name": "Samantha Smith", "gender": "Female", "school": "Harvard"},
    {"name": "Samantha Smith", "gender": "Female", "school": "Harvard"},
]

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify({"members": members})

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    if member_id < len(members):
        return jsonify(members[member_id])
    else:
        return jsonify({"message": "Member not found"})

# This block ensures that the Flask app is only run when executing this file directly,
# and not when imported as a module.
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
