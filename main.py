from flask import Flask, request, jsonify

# Initializing Flask
app = Flask(__name__)

# A more realistic route
@app.route('/get-user/<user_id>') # after the second '/' we initialize something known as a path parameter which allows us to dynamically pass in a value that we can then access in the route
def get_user(user_id):
    # example data:
    user_data = {"user_id" : user_id,
                 "name": "Rohit Truesdale",
                 "email": "rohit.trues@gmail.com"}


# Running our Flask Application
if __name__ == "__main__":
    app.run(debug=True)