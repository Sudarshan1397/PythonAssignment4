try:
    with open("sample.txt","r") as fh:
        lines = fh.readlines()
        for line in lines:
            print(f"Lines : {line.rstrip('\n')}")
except FileNotFoundError:
    print("File that you are trying to open does not exist")