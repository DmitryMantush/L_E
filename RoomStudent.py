import json


with open('rooms.json') as r:
    rooms = json.load(r)
with open('students.json') as s:
    students = json.load(s)

for room in rooms:
    room['students'] = []
    for st in students:
        if st['room'] == room['id']:
            room['students'].append(st)  # collecting students in their rooms by matching id`s

for r in rooms:
    print(r['name'])
    print('-------------------------')
    for st in r['students']:
        print(st['id'], ':', st['name'])
    print('\n\n')



