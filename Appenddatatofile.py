with open("output.txt", "a") as fh:
    fh.write("\na mode is used to append content to the existing file\n")
    fh.write("Good bye")

try:
    with open("output.txt","r") as fh:
        lines = fh.readlines()
        for line in lines:
            print(f"Lines : {line.rstrip('\n')}")
except FileNotFoundError:
    print("File that you are trying to open does not exist")