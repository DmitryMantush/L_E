import json
from collections import defaultdict


class DataProcessing:
    def __init__(self, data):
        self.data = data


class DataIn(DataProcessing):
    def load(self):
        with open(self.data) as f:  # .json
            return json.load(f)


class DataOut(DataProcessing):
    def dump(self, file_name: str):
        with open(f'{file_name}.json', 'w') as f:
            json.dump(self.data, f, indent=2)


rooms = DataIn('rooms.json').load()
students = DataIn('students.json').load()

for room in rooms:
    room['students'] = []
    for st in students:
        if st['room'] == room['id']:
            room['students'].append(st)  # collecting students in their rooms by matching id`s

# for st in students:
#     print(st)
# for r in rooms:
#     print(r)

# dump('rooms_students', rooms)
