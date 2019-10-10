from collections import defaultdict

students = [
    {
        'id': 1,
        'name': 'Nikita #1',
        'room': 1
    },
    {
        'id': 2,
        'name': 'Nikita #2',
        'room': 1
    },
    {
        'id': 3,
        'name': 'Nikita #3',
        'room': 2
    },
    {
        'id': 4,
        'name': 'Nikita #4',
        'room': 2
    },
    {
        'id': 5,
        'name': 'Nikita #5',
        'room': 2
    },
    {
        'id': 6,
        'name': 'Nikita #6',
        'room': 2
    },
    {
        'id': 7,
        'name': 'Nikita #7',
        'room': 3
    }
]

rooms = [
    {
        'id': 1,
        'name': 'Room #1',
        'students': []
    },
    {
        'id': 2,
        'name': 'Room #2',
        'students': []
    },
    {
        'id': 3,
        'name': 'Room #3',
        'students': []
    }
]

rooms_students = defaultdict(list)  # if room does not exist returns empty list

for room in rooms:
    for stud in students:
        if stud['room'] == room['id']:
            room['students'].append(stud['id'])  # collecting students in their rooms by matching id`s
    rooms_students[room['name']] = room['students']

print(rooms_students)
