from chalice import Chalice

from chalicelib import excersises_db, workouts_db

app = Chalice(app_name="backend")
_EXERCISESS_DB = None
_WORKOUTS_DB = None


def get_exercises_db():
    global _EXERCISESS_DB
    # TODO: replace with DynamoDB table
    if not _EXERCISESS_DB:
        _EXERCISESS_DB = excersises_db.InMemoryExerciseDB()
    return _EXERCISESS_DB


def get_workouts_db():
    global _WORKOUTS_DB
    # TODO: replace with DynamoDB table
    if not _WORKOUTS_DB:
        _WORKOUTS_DB = workouts_db.InMemoryWorkoutsDB()
    return _WORKOUTS_DB


@app.route("/")
def index():
    return {"hello": "world"}


@app.route("/exercises")
def list_exercises():
    return get_exercises_db().list_items()


@app.route("/exercises/{uid}")
def get_exercise(uid):
    return get_exercises_db().get_item(uid)


@app.route("/exercises", methods=["POST"])
def create_exercise():
    payload = app.current_request.json_body
    return get_exercises_db().create_item(name=payload["name"])


@app.route("/exercises/{uid}", methods=["PUT"])
def update_exercise(uid):
    payload = app.current_request.json_body
    return get_exercises_db().update_item(uid, name=payload["name"])


@app.route("/exercises/{uid}", methods=["DELETE"])
def delete_exercise(uid):
    return get_exercises_db().delete_item(uid)


@app.route("/workouts")
def list_workouts():
    return get_workouts_db().list_items()


@app.route("/workouts/{uid}")
def get_workout(uid):
    return get_workouts_db().get_item(uid)


@app.route("/workouts", methods=["POST"])
def create_workout():
    payload = app.current_request.json_body
    return get_workouts_db().create_item(
        excercise_uid=payload["exercise_uid"],
        weight=payload["weight"],
        reps=payload["reps"],
    )


@app.route("/workouts/{uid}", methods=["PUT"])
def update_workout(uid):
    payload = app.current_request.json_body
    return get_workouts_db().update_item(
        uid=uid,
        weight=payload["weight"],
        reps=payload["reps"],
    )


@app.route("/workouts/{uid}", methods=["DELETE"])
def delete_workout(uid):
    return get_workouts_db().delete_item(uid)


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
