import json


def load(z):  # .json
    with open(z) as f:
        return json.load(f)


def dump(file_name: str, d: dict):
    with open(f'{file_name}.json', 'w') as f:
        json.dump(d, f, indent=2)


rooms = load('rooms.json')
students = load('students.json')

for room in rooms:
    room['students'] = []
    for st in students:
        if st['room'] == room['id']:
            room['students'].append(st)  # collecting students in their rooms by matching id`s

dump('rooms_students', rooms)
