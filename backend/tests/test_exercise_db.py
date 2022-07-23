from sre_constants import ANY
import pytest
import unittest.mock as mock
from chalicelib.excersises_db import InMemoryExerciseDB


@pytest.fixture
def setup():
    db_dict = {}
    db = InMemoryExerciseDB(db_dict)

    yield db
    db.items = {}


def test_list_items(setup):
    db = setup
    db.create_item("Leg press")
    db.create_item("Squat")
    exercises = db.list_items()

    assert len(exercises) == 2
    assert exercises == [
        {"uid": mock.ANY, "name": "Leg press"},
        {"uid": mock.ANY, "name": "Squat"},
    ]


def test_retrieve_item(setup):
    db = setup
    item = db.create_item("Leg press")
    expected = {"uid": mock.ANY, "name": "Leg press"}

    assert db.get_item(item) == expected


def test_delete_item(setup):
    db = setup
    item = db.create_item("Leg press")
    db.delete_item(item)

    assert len(db._items) == 0


def test_update_item(setup):
    db = setup
    item = db.create_item("Leg pr")
    db.update_item(item, "Leg press")

    assert db._items[item]["name"] == "Leg press"


def test_teardown(setup):
    db = setup
    assert len(db._items) == 0
