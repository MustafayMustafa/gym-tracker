from chalice import Chalice
from chalicelib import excersises_db


app = Chalice(app_name="backend")


@app.route("/")
def index():
    return {"hello": "world"}


@app.route("/exercises")
def list_exercises():
    pass


@app.route("/exercises/{uid}")
def get_exercise(uid):
    pass


@app.route("/exercises", methods=["POST"])
def create_exercise():
    pass


@app.route("/exercises/{uid}", methods=["PUT"])
def update_exercise(uid):
    pass


@app.route("/exercises/{uid}", methods=["DELETE"])
def delete_exercise(uid):
    pass


@app.route("/workouts")
def list_workouts():
    pass


@app.route("/workouts/{uid}")
def get_workout(uid):
    pass


@app.route("/workouts", methods=["POST"])
def create_workout():
    pass


@app.route("/workouts/{uid}", methods=["PUT"])
def update_workout(uid):
    pass


@app.route("/workouts/{uid}", methods=["DELETE"])
def delete_workout(uid):
    pass


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
