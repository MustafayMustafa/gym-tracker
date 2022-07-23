from uuid import uuid4


class ExerciseDB(object):
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


class InMemoryExerciseDB(ExerciseDB):
    def __init__(self, db_dict=None):
        if db_dict is None:
            db_dict = {}
        self._items = db_dict

    def list_items(self):
        return list(self._items.values())

    def get_item(self, uid):
        return self._items.get(uid)

    def create_item(self, name):
        uid = str(uuid4())
        self._items[uid] = {"uid": uid, "name": name}
        return uid

    def update_item(self, uid, name):
        self._items[uid]["name"] = name
        return self._items[uid]

    def delete_item(self, uid):
        del self._items[uid]
        return True
