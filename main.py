import time

current_room = ""

current_items = {'chesspiece'   : False,
                 'shovel'       : False,
                 'wrench'       : False,
                 'pocket knife' : False}
random_items = ['lighter', 'money', 'telephone']

intro_text = """Welcome to the Observatory on top of the mountain,
you're a researcher doing groundbreaking research on the planet Mars.
This is the main room, there is a lab room and a locker room.
You're hearing a strange sound coming from the Lab room go check it out!
"""

def print_words(text):
    text = text.split("\n")
    for i in text:
        print(i)
        time.sleep(0.5)


def lab_room():
    room_explenation = """After some time you awake in the lab room.
There's been a terrible accident with an expirement using the pods in the room.
The martians in the pods have escaped and want to capture you to send you
to their mother ship.
Escape now to the Main room, and go outside from the Locker room.
"""
    print_words(room_explenation)
    while True:
        command = input("> ")
        command = command.lower()
        if command == "go to main room":
            break


def locker_room():
    room_explenation = """You are in the locker room 
This room has 2 Lockers one for You and one for your Coworker.
"""
    your_locker = """This is your locker, it has your bag and
home clothes there is no time to change into those. There is 
also a notepad.
"""
    coworker_locker = """This is your coworkers locker,
it has his items, a bag and his home clothes, and a lucky Chesspiece
as a token.
"""

    print_words(room_explenation)
    while True:
        command = input("> ")
        command = command.lower()
        if command == "open your locker":
            print_words(your_locker)
        elif command == "open coworkers locker":
            print_words(coworker_locker)
        elif command == "pick up chesspiece":
            print_words("You picked up the chesspiece from your coworkers locker. Go to the Hall quickly.")
            current_items['chesspiece'] = True
            break


def main_gate():
    room_explenation = """You forgot that you locked the main gate,
you must unlock it using 4 levers. The Levers are supposed to be bits
and you remember the combination must mean 13 in decimal numbers.
Pull the Levers to create a binary number that is equal to 13.
"""

    room_cleared = """You have remembered the code correctly and
your binary knowledge came in handy. Go to the Bridge.
"""
    print_words(room_explenation)
    correct_combo = [True, False, True, True]
    current_combo = [False, False, False, False]
    while True:
        command = input("> ")
        command = command.lower()
        if command == "pull the first lever":
            current_combo[0] = True
        elif command == "pull the second lever":
            current_combo[1] = True
        elif command == "pull the third lever":
            current_combo[2] = True
        elif command == "pull the fourth lever":
            current_combo[3] = True
        elif current_combo == correct_combo:
            print_words(room_cleared)
            break





def main():
    print_words(intro_text)
    current_room = "main"
    while True:
        print(current_room)
        command = input("> ")
        command = command.lower()
        if command == "q" or command.lower() == "quit":
            break
        elif current_room == "main" and command == "go to lab room":
            lab_room()
        elif current_room == "main" and command == "go to locker room":
            current_room = "locker"
            locker_room()
        elif current_room == "locker" and command == "go to hall":
            current_room = "hall"
            puzzle_landmine()
        elif current_room == "hall" and command == "go to main gate":
            current_room = "gate"
            main_gate()
        print_words(command)

if __name__ == "__main__":
    main()
