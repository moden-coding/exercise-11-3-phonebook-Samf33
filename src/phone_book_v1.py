# Write your solution here
def search(phonebook):
    searchName = input("name: ")
    if searchName in phonebook:
        print(phonebook[searchName])
    else:
        print("no number")
def add(phonebook):
    addName = input("name: ")
    addNum = (input("number: "))
    phonebook[addName] = addNum
    print("ok!")

def main():
    phonebook = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 1:
            search(phonebook)
        if command == 2:
            add(phonebook)
        if command == 3:
            break
    print("quitting...")

main()