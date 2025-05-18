file = "notes.txt"
notes = []

def welcome(): #this function provides welcome banner for user
    print("""
   ╔════════════════════════════════════╗
   ║              Hello!                ║ 
   ║        Simple Notepad App          ║    
   ║    made by Ibrahimov Etibar Adil   ║ 
   ╚════════════════════════════════════╝
    """)

def add(): #this function made for adding notes to the notepad program
    while True:
        notes_id = input("Enter note ID: ")
        if notes_id == "":
            print("ID cannot be empty! Write an number of ID and try again!")
        elif any(note['id'] == notes_id for note in notes):
            print("This ID already exists! Enter another ID and try again!")
        else:
            break

    while True:
        title = input("Enter title: ")
        if title == "":
            print("Title cannot be empty. Write something and try again!")
        else:
            break

    while True:
        note = input("Enter note: ")
        if note == "":
            print("Note cannot be empty. Write something and try again!")
        else:
            break
    notes.append({'id': notes_id, 'title': title, 'note': note})
    print("Note added successfully.")


def view(): #this function is made for viewing all notes written locally or just loaded from the file
    if not notes:
        print("No notes found.")
    else:
        for note in notes:
            print("-" * 30)
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Note: {note['note']}")
        print("-" * 30)

def search(): #this function makes a search by ID or title of note
    search_method = input("Enter ID or title to search: ").lower()
    found = False
    for note in notes:
        if search_method in note['id'].lower() or search_method in note['title'].lower():
            print("-" * 30)
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Note: {note['note']}")
            print("-" * 30)
            found = True
    if not found:
        print("Note has not found.")

def update(): #this function is made for updating data in the notes
    while True:
        note_id = input("Enter ID of note to update: ")

        for note in notes:
            if note['id'] == note_id:
                change_of_id = input("Do you want to change the ID? (Write Yes or No): ").lower()
                if change_of_id == "yes":
                    while True:
                        new_id = input(f"Enter a new ID: (current ID: {note['id']}): ")
                        if new_id == note['id'] or not any(n['id'] == new_id for n in notes):
                            note['id'] = new_id
                            print("ID has been changed successfully or you entered the same ID!")
                            break
                        else:
                            print("This ID already exists! Enter another ID and try again!")
                else:
                    print("Keeping the same ID")

                while True:
                    new_title = input("Enter new title: ")
                    if new_title == "":
                        print("Title cannot be empty. Write something and try again!")
                    else:
                        note['title'] = new_title
                        break

                while True:
                    new_note = input("Enter new note: ")
                    if new_note == "":
                        print("Note cannot be empty. Write something and try again!")
                    else:
                        note['note'] = new_note
                        break

                print("Note updated.")
                return

        print("Note not found")

def delete(): #this function is made to delete notes
    note_id = input("Enter ID of note to delete: ")
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            print("Note deleted successfully.")
            return
    print("Note not found.")

def save(): #this function provides saving notes and their data into the .txt file
    try:
        file_notes_txt = open(file, "w", encoding="utf-8")
        for note in notes:
            line = f"ID: {note['id']} / Title: {note['title']} / Note: {note['note']}\n"
            file_notes_txt.write(line)
        print("Notes saved to file successfully.")
    except Exception as e:
        print(f" Ooops! Error with saving note(s): {e}")

def load(file): #this function provides loading notes and their data to program from the .txt file
    try:
        file_notes_txt = open(file, "r", encoding="utf-8")
        for line in file_notes_txt:
            parts = line.split(" / ")
            if len(parts) == 3:
                notes.append({'id': parts[0].replace("ID: ", ""),
                              'title': parts[1].replace("Title: ", ""),
                              'note': parts[2].replace("Note: ", "")})
        print("Notes are loaded.")
    except:
        print("No file detected or error.")


def sort_by_title(): #this function is made for sorting notes by their titles
    def get_title(note):
        return note['title'].lower()
    notes.sort(key=get_title)
    print("Notes sorted by title.")

def sort_by_id(): #this function is made for sorting notes by their IDs
    notes.sort(key=lambda note: int(note['id']))
    print("Notes sorted by ID.")

def count(i=0): #this function is made for counting a current amount of exiting notes
    if i >= len(notes):
        return 0
    return 1 + count(i+1)

def help(): #this function is made for giving a help instructions about program to user
    print("""
Help Menu:
- Add note: enter ID, title, and note to add note here
- View notes: see all saved notes that you made recently
- Search: find notes by ID or title
- Update: change title and note of a note by ID, or change ID also!
- Delete: remove a note by ID
- Save/Load: store notes in a text file (.txt)
- Sort by title: sort notes by title due to alphabet
- Sort by ID: sort notes by ID
- Count: count total notes using recursive function
- Clear all: delete all notes
- Exit: end your work and quit the app. Don't forget to save all your notes :)
""")

def clear_all(): #this function is made for deleting ALL the notes from program
    confirm = input("Are you sure? This will delete all notes (Write Yes or No): ").lower()
    if confirm == "yes":
        notes.clear()
        print("All notes deleted.")
    else:
        print("Clear cancelled.")

def menu(): #this function is made for calling main menu of program, showing what it can to do
    print("Menu:")
    print("1. Add note")
    print("2. View all notes")
    print("3. Search note")
    print("4. Update note")
    print("5. Delete note")
    print("6. Save notes to file")
    print("7. Load notes from file")
    print("8. Sort notes by title")
    print("9. Sort notes by ID")
    print("10. Count notes")
    print("11. Help")
    print("12. Clear all notes")
    print("13. Exit")

def main(): #this function is made for controlling choices of user and perform the user's desired tasks correctly
    welcome()
    while True:
            menu()
            choice = input("Choose option you need (1-12): ")
            if choice == "1":
                add()
            elif choice == "2":
                view()
            elif choice == "3":
                search()
            elif choice == "4":
                update()
            elif choice == "5":
                delete()
            elif choice == "6":
                save()
            elif choice == "7":
                load(file)
            elif choice == "8":
                sort_by_title()
            elif choice == "9":
                sort_by_id()
            elif choice == "10":
                print(f"Number of notes: {count()}")
            elif choice == "11":
                help()
            elif choice == "12":
                clear_all()
            elif choice == "13":
                print("Thank you for using!")
                break
            else:
                print("Invalid choice, try again!")
            input("Press Enter to continue...")

main()
