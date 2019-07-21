# just input something from the console and print it out

while True:
    target = raw_input("Name of the target: ")

    if target == "exit":
        break

    print(target)