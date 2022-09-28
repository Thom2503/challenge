import time
import sys

current_room = "" # de huidige kamer waar je nu bent zodat je niet de hele game kan skippen
# dictionary met de items die je nodig hebt. Als het op true staat heb je de item
current_items = {'chesspiece'   : False,
                 'shovel'       : False,
                 'wrench'       : False,
                 'pocket knife' : False}
# random item om de speler in de maling te nemen wat later in het spel
random_items = ['lighter', 'money', 'telephone']
# de tekst waar je mee begint en die het verhaal een beetje uitlegd
intro_text = """Welcome to the Observatory on top of the mountain,
you're a researcher doing groundbreaking research on the planet Mars.
This is the main room, there is a lab room and a locker room.
You're hearing a strange sound coming from the Lab room go check it out!
"""

def print_words(text):
    """
    Functie om een de tekst wat langzamer te laten printen zodat het bij te houden is.

    @param string text - de tekst om langzaam uit te printen
    """
    text = text.split("\n") # split de tekst bij de newline zodat je bij zinnen kan wachten.
    for i in text:
        print(i)
        time.sleep(1) # wacht 1 seconde met het uitprinten van de tekst


def lab_room():
    """
    Functie om voor de labruimte waar de marsmannetjes aanwezig zijn, hier kan je alleen
    maar terug naar de hoofdruimte.
    """
    room_explenation = """After some time you awake in the lab room.
There's been a terrible accident with an expirement using the pods in the room.
The martians in the pods have escaped and want to capture you to send you
to their mother ship.
While they are following you. you look outside it seems like everything still 
the same the bridge still there.
The three flower horses still there, but all the people are gone. 
Escape now to the Main room, and go outside from the Locker room.
If you need some help press H.
"""
    print_words(room_explenation)
    while True:
        command = input("> ")
        command = command.lower()
        if command == "go to main room":
            break


def locker_room():
    """
    Functie om het verhaal van de ruimte met de lockers te geven, daar zijn twee lockers.
    Een voor je collega en een voor jou, hier pak je ook een belangrijk item voor een latere
    puzzel.
    """
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
            current_items['chesspiece'] = True # je hebt nu het schaakstuk gepakt. Dit is optioneel
            break
        elif command == "go to hall":
            break


def main_gate():
    """
    Functie voor de hoofd ingang, dit is een puzzel waar je 4 wissels hebt die een binaire
    code hebben, waar je bij ons geval 13 moet maken.
    """
    room_explenation = """You forgot that you locked the main gate,
you must unlock it using 4 levers. The Levers are supposed to be bits
and you remember the combination must mean 13 in decimal numbers.
Pull the Levers to create a binary number that is equal to 13. 
Try to open the gate.
"""

    room_cleared = """You have remembered the code correctly and
your binary knowledge came in handy. Go to the Bridge.
"""
    print_words(room_explenation)
    correct_combo = [True, False, True, True] # dit is om te checken of de goede wissels zijn omgehaald
    current_combo = [False, False, False, False] # hoe de wissels nu zijn
    while True:
        command = input("> ")
        command = command.lower()
        # als je een van deze kiest wordt die wissel naar True gezet
        if command == "pull the first lever":
            current_combo[0] = True
        elif command == "pull the second lever":
            current_combo[1] = True
        elif command == "pull the third lever":
            current_combo[2] = True
        elif command == "pull the fourth lever":
            current_combo[3] = True
        # als je open gate zegt moet wordt er ook gecheckt of de combinatie goed is
        elif command == "open gate" and current_combo == correct_combo:
            print_words(room_cleared)
            break
        else:
            # zet het weer terug als het niet klopt
            current_combo = [False, False, False, False]
            print_words("You gave the wrong combination...\nThe levers are reset.")


def puzzle_landmine():
    """
    Funcie voor de puzzel met landmijnen, omdat het een beveiligd instituut is, moet je een
    veld landmijnen doorstaan, je moet dus het correcte pad volgen.
    """
    reddoor = """Finally you have made it to the Big Red door.
You decide to walk into the room.
Its dark and can't find the switch for the lights.
After some time you find something that feels like a switch and you pull the lever.
The room is complety empty.
The hear some noise from the room where you came from.
The martians have catched up and now holding you hostage.
Their mothership have now abducted you and you will never see earth again...
"""
    bluedoor = """Finally you have made it to the Big Blue door.
Lets hurry up before the martians are here.
You know the Main gate is a little further.
On the wall is a shovel take it with you it might come in handy.
"""
    start_landmineroom = """You're now in the hall.
In front of you there is a board you decide to check it out.
You are now right in front of the board. it has squares and you have to move over them.
If you want to move on the board type Left, Right, Down or Forward.
"""
    # de correcte volgode van bewegen door het veld met landmijnen
    the_right_moves = [
        'forward',
        'left',
        'forward',
        'forward',
        'right',
        'forward',
        'right',
        'right',
        'foutregel',
        'forward',
        'down'
    ]

    print_words(start_landmineroom)
    counter = 0 

    while counter < 10:   
        user_move = input("> ")
        user_move = user_move.lower()
        if user_move == the_right_moves[counter]:
            print_words("Okay that worked what now.")
            counter += 1
        elif user_move == the_right_moves[9]:
            print_words(reddoor) # de rode deur is niet goed wat lijdt tot een dood einde
            # kan wat mooier maar de game moet afgesloten worden want dit is een einde voor de hoofdpersonage
            sys.exit("You lost the game!")
        elif user_move == the_right_moves[10]:
            print_words(bluedoor)
            current_items['shovel'] = True # De shovel is een soort hulp bij de derde puzzel wat een foutieve brug is.
            break
        else:
            print_words("BOOM you stepped on a mine try agian!")
            counter = 0 # zet de counter weer op 0 want je moet opnieuw proberen

#TODO kijken of de namen kloppen
def hint():

    counter = 0

    while counter == 0:
        if input == "h":
            if current_room == "main room":
                print("Have you tried goin to the sound maybe someone can help you there.")
            if current_room == "lab room":
                print("Have you tried going back. Martians can be scary.")
            if current_room == "locker room":
                print("Have you tried opening the locker maybe somethings inside.")
            if current_room == "hall":
                print("Have you tried not stepping on a mine.\n  or remember the patern.")
            if current_room == "main gate":
                print("Have you tried opening the gate when you think it's right.")
            if current_room == "bridge":   
                print("Have you tried not falling to your death.")   
            if current_room == "chessboard":  
                print("Have you tried doing the first move you would set.")
        

def main():
    """
    De main game loop waar eigenlijk alles gebeurt en wordt aangeroepen.
    """
    # print de intro met een beetje backstory
    print_words(intro_text)
    current_room = "main" # zet de huidige kamer op main dat is waar je start
    # blijf voor eeuwig loopen tot er wordt gezegt dat de speler wilt stoppen
    # of wanneer de game is afgelopen
    while True:
        # vraag de input van de speler om te bepalen wat er dan moet gebeuren.
        # zet dit naar lowercase zodat je niet voor alle rand gevallen hoeft te checken.
        command = input("> ")
        command = command.lower()
        # als je de game wilt eindigen.
        if command in ("q", "quit"):
            break
        if current_room == "main" and command == "go to lab room":
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
