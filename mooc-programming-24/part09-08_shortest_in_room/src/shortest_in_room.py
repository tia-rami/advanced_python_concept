# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.person_list = []
        self.combined_height = 0

    def add(self, person: Person):
        self.person_list.append(person)
        self.combined_height += person.height


    def is_empty(self):
        return len(self.person_list) == 0

    def print_contents(self):
        print(f"There are {len(self.person_list)} persons in the room, and their combined height is {self.combined_height} cm")
        for person in self.person_list:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if self.is_empty():
            return None

        shortest = self.person_list[0]
        for person in self.person_list:
            if shortest.height > person.height:
                shortest = person
        
        return shortest

    def remove_shortest(self):
        if self.is_empty():
            return None
        shortest = self.shortest()
        shortest_index = self.person_list.index(shortest)
        return self.person_list.pop(shortest_index)

if __name__ == "__main__":
    room = Room()
    # print("Is the room empty?", room.is_empty())
    # print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    removed = room.remove_shortest()
    # print("Is the room empty?", room.is_empty())
    # print("Shortest:", room.shortest())
    print(f"Removed from room: {removed.name}")
    
    print()

    room.print_contents()