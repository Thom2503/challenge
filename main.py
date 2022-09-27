def main():
    while True:
        command = input("> ")
        if command.lower() == "q" or command.lower() == "quit":
            break

        print(command)

if __name__ == "__main__":
    main()
