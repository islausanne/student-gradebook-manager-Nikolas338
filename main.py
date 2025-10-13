


def start():
    choice = input("\nSelect option: \n 1. Read files\n 2. Write files\n 3. Search\n 4. Modify\n 5. Exit\n")
    if choice == "1":
        readfile()
    elif choice == "2":
        writefile()
    elif choice == "3":
        searchfile()
    elif choice == "4":
        modifyfiles()
    elif choice == "5":
        exit("Program Terminated")
    else:
        print("Invalid choice")


def readfile():
    with open("studentfile.txt","a"):
        pass

    with open("studentfile.txt","r") as s:
        for line in s:
            parts = [x.strip() for x in line.strip().split(",")]
            print(" ".join(parts))  # prints cleanly
        start()

def writefile():
    name = input("Enter name: ")
    grade = input("Enter grade: ")
    with open("studentfile.txt","a") as s:
        s.write(f"\n{name},{grade}")
    start()

def searchfile():
    found = False
    name = input("Enter name: ")
    with open("studentfile.txt","r") as s:
        for line in s:
            if name in line:
                print(line)
                found = True

    if not found:
        print("Name not found")
    else:
        print("Name found")
    start()

def modifyfiles():
    choice = input("Choose option: \n1. Modify grade \n2. Delete student\n3. Exit\n")
    if choice == "1":
        modifygrade()
    elif choice == "2":
        pass
    elif choice == "3":
        start()
    start()

def modifygrade():
    data = []
    with open("studentfile.txt", "r") as s:
        for line in s:
            parts = [x.strip() for x in line.strip().split(",")]
            if len(parts) == 2:
                data.append(parts)

    name = input("Enter name: ").strip()
    nameindex = -1

    for i, record in enumerate(data):
        if record[0].lower() == name.lower():
            nameindex = i
            break

    if nameindex == -1:
        print("Name not found.")
    else:
        newgrade = input(f"Enter new grade for {data[nameindex][0]} (old grade: {data[nameindex][1]}): ")
        data[nameindex][1] = newgrade  # update the grade

        # Write updated data back to the file
        with open("studentfile.txt", "w") as s:
            for record in data:
                s.write(f"{record[0]},{record[1]}\n")

        print("Grade updated successfully.")

    start()


start()