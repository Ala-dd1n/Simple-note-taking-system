notes = []

def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({"title": title, "content": content})
    print("Note saved")

def view_notes():
    if not notes:
        print("No notes available")
    else:
        for note in notes:
            print("Title:", note["title"])
            print("Content:", note["content"])
            print("----------------")

def main():
    while True:
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
