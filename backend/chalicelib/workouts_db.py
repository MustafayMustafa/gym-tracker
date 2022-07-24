from uuid import uuid4


class WorkoutsDB(object):
    def list_items(self):
        pass

    def get_item(self, uid):
        pass

    def create_item(self, name):
        pass

    def update_item(self, uid, name):
        pass

    def delete_item(self, uid):
        pass


class InMemoryWorkoutsDB(WorkoutsDB):
    def __init__(self, db_dict=None):
        if db_dict is None:
            db_dict = {}
        self._items = db_dict

    def list_items(self):
        return list(self._items.values())

    def get_item(self, uid):
        return self._items.get(uid)

    def create_item(self, excercise_uid: str, weight: int, reps: int):
        uid = str(uuid4())
        self._items[uid] = {
            "uid": uid,
            "excercise": excercise_uid,
            "sets": [{"weight": weight, "reps": reps}],
        }
        return uid

    def update_item(self, uid, weight: int, reps: int):
        self._items[uid]["sets"].append({"weight": weight, "reps": reps})
        return self._items[uid]

    def delete_item(self, uid):
        del self._items[uid]
        return True
