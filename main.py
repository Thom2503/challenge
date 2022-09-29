from glob import escape
import time
import sys
import random

current_room = "" # de huidige kamer waar je nu bent zodat je niet de hele game kan skippen
not_valid = "Not a valid command" # error als je niet een goed commando doorgeeft
# dictionary met de items die je nodig hebt. Als het op true staat heb je de item
current_items = {'chesspiece'   : False,
                 'shovel'       : False,
                 'wrench'       : False,
                 'pocket knife' : False}
# random item om de speler in de maling te nemen wat later in het spel
random_items = ['Lighter', '10 Euro Bill', 'Telephone']
title = """
 _______ _       __          __                   _   _           ____  _                              _                   
|__   __| |      \ \        / /                  | | | |         / __ \| |                            | |                  
   | |  | |__   __\ \  /\  / /_ _ _ __ ___  _ __ | |_| |__   ___| |  | | |__  ___  ___ _ ____   ____ _| |_ ___  _ __ _   _ 
   | |  | '_ \ / _ \ \/  \/ / _` | '__/ _ \| '_ \| __| '_ \ / _ \ |  | | '_ \/ __|/ _ \ '__\ \ / / _` | __/ _ \| '__| | | |
   | |  | | | |  __/\  /\  / (_| | | | (_) | | | | |_| | | |  __/ |__| | |_) \__ \  __/ |   \ V / (_| | || (_) | |  | |_| |
   |_|  |_| |_|\___| \/  \/ \__,_|_|  \___/|_| |_|\__|_| |_|\___|\____/|_.__/|___/\___|_|    \_/ \__,_|\__\___/|_|   \__, |
                                                                                                                      __/ |
                                                                                                                     |___/
By: Thom and Robin :)
"""
# de tekst waar je mee begint en die het verhaal een beetje uitlegd
intro_text = f"""
{title}

Welcome to the Observatory on top of the mountain,
you're a researcher doing groundbreaking research on the planet Mars.
This is the main room, there is a lab room and a locker room.
You're hearing a strange sound coming from the Lab room go check it out!

If you need some help press h or type help.
"""

def hint(room):
    """
    Functie om een hint te geven per ruimte.
    @param string room - voor welke kamer de hint is
    """
    if room == "main":
        print_words("Have you tried going to the sound maybe someone can help you there.")
    elif room == "lab":
        print_words("Have you tried going back. Martians can be scary.")
    elif room == "locker":
        print_words("Do you know that your coworker has a token?")
    elif room == "hall":
        print_words("Have you tried not stepping on a mine.\n  or remember the patern.")
    elif room == "main gate":
        print_words("Have you tried opening the gate when you think it's right.")
    elif room == "bridge":   
        print_words("Have you tried to remember what you found?")   
    elif room == "chessboard":  
        print_words("Have you tried doing the first move you would set.")
    elif room == "barn":  
        print_words("Have you tried looking around maybe you can find something.")


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
"""
    print_words(room_explenation)
    while True:
        command = input("> ")
        command = command.lower()

        if command in ("h", "help"):
            hint("lab")
        elif command == "go to main room":
            break


def locker_room():
    """
    Functie om het verhaal van de ruimte met de lockers te geven, daar zijn twee lockers.
    Een voor je collega en een voor jou, hier pak je ook een belangrijk item voor een latere
    puzzel.
    """
    room_explenation = """You are in the locker room
This room has 2 Lockers one for You and one for your Coworker.
The martians are on your tail maybe go straight to the Hall,
or check the Lockers, but maybe you don't have the time?
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
    locker_open = False
    while True:
        command = input("> ")
        command = command.lower()
        if command in ("h", "help"):
            hint("locker")
        elif command == "open your locker":
            print_words(your_locker)
        elif command == "open coworkers locker":
            print_words(coworker_locker)
            locker_open = True
        elif command == "pick up chesspiece" and locker_open:
            print_words("You picked up the chesspiece from your coworkers locker. Go to the Hall quickly.")
            current_items['chesspiece'] = True # je hebt nu het schaakstuk gepakt. Dit is optioneel
        elif command == "go to hall":
            print_words("You see a Square on the ground walk up to it.")
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
Try to Open the Gate.
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
        if command in ("h", "help"):
            hint("main gate")
        # als je een van deze kiest wordt die wissel naar True gezet
        elif command == "pull the first lever":
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
You know the Main Gate is a little further.
On the wall is a Shovel take it with you it might come in handy.
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
        if user_move in ("h", "help"):
            hint("hall")
            continue
        if user_move == the_right_moves[counter]:
            print_words("Okay that worked what now.")
            counter += 1
        elif counter == 6 and user_move == the_right_moves[9]:
            print_words(reddoor) # de rode deur is niet goed wat lijdt tot een dood einde
            # kan wat mooier maar de game moet afgesloten worden want dit is een einde voor de hoofdpersonage
            sys.exit("You lost the game!")
        elif counter == 8 and user_move == the_right_moves[10]:
            print_words(bluedoor)
            current_items['shovel'] = True # De shovel is een soort hulp bij de derde puzzel wat een foutieve brug is.
            break
        else:
            print_words("BOOM you stepped on a mine try agian!")
            counter = 0 # zet de counter weer op 0 want je moet opnieuw proberen

def chessboard():
    introduction = """After the bridge you walked to the maze.
Not a big one like you thought but you still needed to find your way thougth the bushes.
You have found your way through this difficult maze and you see a chessboard.
There is a sign next to it.
'The Legendary Game of Chess'
'You can only do one move to prove your worthy.'
"""
    no_piece = """The sign changed it's text suddenly,
'You haven't looked in your Coworkers Locker, huh?'.
The martians are now coming fastly towards you. With nowhere to go,
you just wait out your luck and get captured by the martians.
"""
    outro = """You have proved that your worthy,
The martians are coming you look around where to go next.
In the distance you can see smoke of what appears to be a Campsite head 
over it to find out where it's coming from.
"""
    print_words(introduction)
    counter = 0
    if current_items['chesspiece'] == False:
        print_words(no_piece)
        sys.exit("You lost the game!")
    while counter == 0:
        print_words("What first move do you want to set?")
        first_move = input("> ")
        #als de move f3 is dan kan je verder dit heb ik in het verhaal van dat als je wakker word gestopt
        if first_move in ("h", "help"):
            hint("chessboard")
            continue
        if first_move == "f3":
            print_words(outro)
            counter += 1
        else:
            print_words("The sign changed, 'your not worthy'. Try again.")
        if counter == 10:
            print_words("you see the martians run up to you, you have one and only one final guess make it a good one.")
            if first_move == "f3":
                print_words(outro)
            else:
                print_words("The martians have now abducted you to their mothership. \n Maybe you see the right move now.")
        

def bridge():
    """
    Functie voor de brug, dit is een puzzel waar je op de correcte planken van de brug moet lopen.
    Je kan dit 'overslaan' door je schep te gebruiken bij elke plank
    """
    room_explenation = """You have made it to the bridge, although it
is not the bridge you remember. The bridge is partly broken, and it is a
rope bridge now. Because the bridge is broken you have to choose the right
planks to walk on. You can Skip 1 plank or Walk on it.
"""
    death_text = """"Unfortunatly you have stepped on the wrong plank.
That was you short and sweet life, at least you were doing groundbreaking
research that will help mankind someday.
"""
    cleared_room = """You have made it safely across the bridge, that was
a tough one. You can hear the martians behind you, hurry to the weird Maze.
"""
    print_words(room_explenation)
    # de correcte stappen om te nemen.
    correct_planks = [True, False, True, True, True, False]
    your_moves = []
    i = 0
    times_used = 0
    bridge_len = len(correct_planks)
    # kan mooier dan alleen true
    while i < bridge_len:
        command = input("> ")
        command = command.lower()
        if command in ("h", "help"):
            hint("bridge")
            continue
        # je kan checken met je schep of het een plank veilig is
        if command == "use shovel":
            # het moet niet te OP zijn dus na twee keer hard drukken gaat het kapot
            if times_used == 2:
                print_words("You can't use the shovel because it broke...")
                continue
            # test of het een gebroken plank is
            if correct_planks[i] is False:
                print_words("The plank that you tested was a broken one,\nbeter Skip it!")
            else:
                print_words("The plank that you tested was not broken it's safe to Walk over!")
            times_used += 1
            continue
        
        if command == "skip":
            your_moves.append(False)
        elif command == "walk":
            your_moves.append(True)
        else:
            print_words(not_valid)
            continue
        # check of je huidige move correct is
        if your_moves[i] != correct_planks[i]:
            print_words(death_text)
            sys.exit("You lost the game!")
        # als alle moves correct zijn ga dan door
        if your_moves == correct_planks:
            print_words(cleared_room)
            break
        print_words(f"Good {bridge_len - i - 1} planks to go")
        i += 1


def campsite():
    """
    Functie waar een klein verhaaltje wordt verteld over paar bergbeklimmers waar iets
    mysterieus fout is gegaan waardoor alleen hun spullen en tenten enz. zijn achtergelaten.
    De speler krijgt hier een random item en een wrench.
    """
    # dit is de random item die de speler krijgt.
    random_item = random.choice(random_items)
    current_items['wrench'] = True
    
    room_explenation = f"""From following the smoke you enter
an abandoned campsite, with 3 tents, a fire with a stove and some gear.
You look around for the mountain climbers but they have vanished.

Pondering what to do you look arround in the tents to find some bags,
you look in one and you find a {random_item} and a Wrench. 
Maybe this can be used.

You look around some more to know for sure that the mountain climbers
are gone but to no avail.

The only thing you know is that there are martians coming after you,
one is already audible so better move fast and go through some more
Woods to the base of the mountain.
"""
    print_words(room_explenation)

def barn():
    intro = """After some time walking you made it to the base of the mountain,
wherer you see something that looks like a barn. You decide to enter it, inside are some Tools and a Tractor.
You remember that is was supposed to be your Volvo V60.
Maybe you can repair the Tractor to make sure you can leave this place as fast as possible.
"""

    looking = """You look around in the barn to look for
extra useful items. There is a lot of junk. So naturally 
the only thing you can find is a somewhat old and rusted pocket knife. 
This can come in handy later...
"""

    open_hood = """You open the hood, the first thing you see is that the Transmission is broken. 
Maybe if you use the Tools you found you can Fix the Transmission.
"""

    fixing_transmission = """You remember that you picked up the Wrench from 
the dissappeard mountain climbers. Using this Wrench you poke around to find the correct nut.
Fastening the nut use the Wrench, after some difficulty, the Tranmission is working now.
Now you can get in the Tractor and drive to Exit the Barn.
"""

    print_words(intro)
    current_items['pocket knife'] = True
    is_fixed = False
    opened_hood = False
    while is_fixed == False:
        command = input("> ")
        command = command.lower()

        if command in ("h", "help"):
            hint("barn")
            continue
        elif command == "look around":
            print_words(looking)
        elif command == "open hood":
            print_words(open_hood)
            opened_hood = True
        elif command == "fix transmission" and opened_hood:
            print_words(fixing_transmission)
            is_fixed = True
        else:
            print_words(not_valid)


def ending():
    escaped_text = """You try countless times to stab the martian, but he
blocks every attempt. After some time you begin to notice that he is easily
distracted, so you say that there is a beatiful martian lady waiting for
the martian in a bar. This makes the martian think.

Now is the time to stab the martian. You manage to grab the knife and stab the 
martian in the neck, and push out of the Tractor. The others are too slow to 
catch up and you escape.

Only it's actually too late, their mothership has arrived and in one fell swoop
your being taken to mars.



      PART TWO COMING SPRING NEXT YEAR
    -= THE ESCAPE FROM THE MOTHERSHIP =-

"""

    awake_text = """The martian knocks the knife out of your hand. You stand no chance, he stronger, bigger, and smarter.
He gets in the Tractor and starts to scratch you. You lose control of the Tractor and crash into a tree.
Before the martian will eat you he tells you a story about how his civilization will colonize and destroy earth 
to use all of its inhabitants to gather materials.
When his story is over he says that you have seen too much and has to kill you. It happens fast.

You suddenly wake up, you think it was a dream, but you look around to see if you're in a familiar environment.
This is not a familiar place, the room is shiny and with a lot of probes. You're on an operating table of the 
martians. "Oh shit" you think.


      PART TWO COMING SPRING NEXT YEAR
    -= THE ESCAPE FROM THE MOTHERSHIP =-
"""

    random_end = escaped_text if random.randint(1,2) == 2 else awake_text

    ending_text = f"""You're exiting the barn, you can hear some of
the martians, and see them in your rear mirror. One is pretty fast which you didn't
expect.

He jumps with you in the Tractor and begins to attack you to stop the Tractor and 
capture you. You take one hand from the steering wheel and you begin to grab for
the old and rusted pocket knife. You begin to stab the martian.

{random_end}
"""
    print_words(ending_text)


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
        if command in ("h", "help"):
            hint("main")
            continue
        if current_room == "main" and command == "go to lab room":
            lab_room()
            print_words("Good the Locker room is in sight. That's where the exit is.")
        elif current_room == "main" and command == "go to locker room":
            current_room = "locker"
            locker_room()
        elif current_room == "locker" and command == "go to square":
            current_room = "hall"
            puzzle_landmine()
        elif current_room == "hall" and command == "go to main gate":
            current_room = "gate"
            main_gate()
        elif current_room == "gate" and command == "go to bridge":
            current_room = "bridge"
            bridge()
        elif current_room == "bridge" and command == "go to maze":
            current_room = "chessboard"
            chessboard()
        elif current_room == "chessboard" and command == "go to campsite":
            current_room = "campsite"
            campsite()
        elif current_room == "campsite" and command == "go through woods":
            current_room = "barn"
            barn()
        elif current_room == "barn" and command == "exit barn":
            ending()
        else:
            print_words(not_valid)

if __name__ == "__main__":
    main()

