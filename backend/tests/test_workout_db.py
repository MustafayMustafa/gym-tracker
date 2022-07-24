import unittest.mock as mock

import pytest
from chalicelib.workouts_db import InMemoryWorkoutsDB


@pytest.fixture
def setup_workouts_db():
    db_dict = {}
    db = InMemoryWorkoutsDB(db_dict)

    yield db
    db.items = {}


def test_list_items(setup_workouts_db):
    db = setup_workouts_db

    db.create_item(excercise_uid="123", weight=100, reps=5)
    db.create_item(excercise_uid="456", weight=160, reps=8)

    workouts = db.list_items()
    assert len(workouts) == 2
    assert workouts == [
        {"uid": mock.ANY, "excercise": "123", "sets": [{"weight": 100, "reps": 5}]},
        {"uid": mock.ANY, "excercise": "456", "sets": [{"weight": 160, "reps": 8}]},
    ]


def test_retrieve_item(setup_workouts_db):
    db = setup_workouts_db
    item = db.create_item(excercise_uid="123", weight=100, reps=5)
    expected = {
        "uid": mock.ANY,
        "excercise": "123",
        "sets": [{"weight": 100, "reps": 5}],
    }

    assert db.get_item(item) == expected


def test_delete_item(setup_workouts_db):
    db = setup_workouts_db
    item = db.create_item(excercise_uid="123", weight=100, reps=5)
    db.delete_item(item)

    assert len(db._items) == 0


def test_update_item(setup_workouts_db):
    db = setup_workouts_db
    item = db.create_item(excercise_uid="123", weight=100, reps=5)
    db.update_item(item, weight=160, reps=8)

    assert db._items[item]["sets"] == [
        {"weight": 100, "reps": 5},
        {"weight": 160, "reps": 8},
    ]
