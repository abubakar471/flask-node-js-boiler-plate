from flask import Flask, request
import json

# setup flask server
app = Flask(__name__)

# Setup url route which will calculate total sum of array.


@app.route('/arraysum', methods=['POST'])
def sum_of_array():
    data = request.get_json()
    print(data)

    # Data variable contains the
    # data from the node server
    ls = data['array']
    result = sum(ls)

    # Return data in json format
    return json.dumps({"result": result})

@app.route("/hello", methods=["GET"])
def hello():
    print("hello");

    return json.dumps({"message" : "hello"})

if __name__ == "__main__":
    app.run(port=5000)
