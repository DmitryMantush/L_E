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


class Packer(DataProcessing):

    def pack(self):
        res = defaultdict(list)
        for el in self.data:
            res[el['room']].append(el)
        return res


def main():
    rooms = DataIn('rooms.json').load()
    students = DataIn('students.json').load()
    stud_by_rooms = Packer(students).pack()
    for room in rooms:
        room['students'] = stud_by_rooms[room['id']]
    DataOut(rooms).dump('rooms_students')


if __name__ == '__main__':
    main()
