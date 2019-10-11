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

for r in rooms:  # report about rooms and students living
    print(r['name'])
    print('-------------------------')
    for st in r['students']:
        del st['room']  # we don`t need room id`s in students profiles any more
        print(st['id'], ':', st['name'])
    print('\n\n')

with open('rooms_students.json', 'w') as file:
    json.dump(rooms, file, indent=2)
