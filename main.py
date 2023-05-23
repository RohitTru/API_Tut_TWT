from flask import Flask, request, jsonify

# Initializing Flask
app = Flask(__name__)

# A Get route Example;
@app.route('/get-user/<user_id>') # after the second '/' we initialize something known as a path parameter which allows us to dynamically pass in a value that we can then access in the route
def get_user(user_id):
    # example data:
    user_data = {"user_id" : user_id,
                 "name": "Rohit Truesdale",
                 "email": "rohit.trues@gmail.com"}
    # Query parameter
    extra =request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200 # jsonify: javascript object notation which is essentially a python dictionary in javascript. This allows a flask to parse our dictionary and return it in json to show the user. The 200 we pass is a status code that means success

# A post route:
@app.route('/create-user', methods =["POST"])
def create_user():
    data = request.get_json()
    
    return jsonify(data), 201

# Running our Flask Application
if __name__ == "__main__":
    app.run(debug=True)