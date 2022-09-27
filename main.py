
def puzzle_landmine():
    '''
    you have made it to the first room. it seems like there are mines everywhere. maybe if we find the right way we can moce past them.
    '''
#nog verhaal omheen verzinnen
    reddoor = """finally you have made it to the Big Red door
"""
    bluedoor = """finally you have made it to the Big Blue door
"""
    start_landmineroom = """you are now right in front of the board. if you want to move an the board type left, right, down or forward
"""

    the_right_moves = [
        "forward",
        "left",
        "forward",
        "forward",
        "right",
        "forward",
        "right",
        "right",
        "foutregel",
        "forward",
        "down"

]

    print(start_landmineroom)
    counter = 0 

    while counter < 10:   
        user_move = input("what move do you want to do")
        if user_move == the_right_moves[counter]:
            print("okay that worked what now")
            counter += 1
        elif user_move == the_right_moves[9]:
            print(reddoor)
        elif user_move == the_right_moves[10]:
            print(bluedoor)
        else:
            print("BOOM you stepped on a mine try agian!")
puzzle_landmine()

def main():
    while True:
        command = input("> ")
        if command.lower() == "q" or command.lower() == "quit":
            break

        print(command)

if __name__ == "__main__":
    main()


