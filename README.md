# PythonAssignment4
Task1
# Below program i have used try except block because if file does not exists program will terminate abruptly and its not good practice 
try:
    with open("sample.txt","r") as fh:        # I have used with function to open file so that i does not have close the file manually
        lines = fh.readlines()                # readlines() function reads all the lines of the file at ones 
        for line in lines:                    # used for loop to prints all the lines of the file
            print(f"Lines : {line.rstrip('\n')}")                    # line.rstrip() function removes space to the right side of line, here we have removed last '\n' of the line
except FileNotFoundError:                                            # If there is exception in the try block execpt catches that exxeption and execute except block if there is no exception except will not execute
    print("File that you are trying to open does not exist")

Task2
# I have used with function to open file so that i does not have close the file manually here there is no need for try block because a mode creates new file if it does not exists
with open("output.txt", "a") as fh:
    fh.write("\na mode is used to append content to the existing file\n")
    fh.write("Good bye")

try:
    with open("output.txt","r") as fh:        # I have used with function to open file so that i does not have close the file manually
        lines = fh.readlines()                # readlines() function reads all the lines of the file at ones 
        for line in lines:                    # used for loop to prints all the lines of the file
            print(f"Lines : {line.rstrip('\n')}")                    # line.rstrip() function removes space to the right side of line, here we have removed last '\n' of the line
except FileNotFoundError:                                            # If there is exception in the try block execpt catches that exxeption and execute except block if there is no exception except will not execute
    print("File that you are trying to open does not exist")
