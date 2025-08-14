import json
import os
from pathlib import Path

FILE_NOTE = Path('notes.json')

notes_list = []


def load_notes():
    if os.path.exists(FILE_NOTE):
        try:
            with open(FILE_NOTE, 'r') as nf:
                notes_list.extend(json.load(nf))
        except json.JSONDecodeError:
            notes_list.clear()
    else:
        FILE_NOTE.touch()
        notes_list.clear()
    return notes_list


load_notes()


def show_notes():
    pass


def search_note():
    pass


def add_note():
    new_note_title = input('Enter the title of your note: ').strip()
    new_note_content = input('Enter the content of your note: ').strip()
    if new_note_title and new_note_content:
        new_note = {'id': len(notes_list)+1,
                'title': new_note_title, 'content': new_note_content}
        notes_list.append(new_note)
        print('Note successfully added.')
    else:
        print('Note can\'t be empty.')


def delete_note():
    pass


def save_notes():
    with open(FILE_NOTE, 'w') as nf:
        json.dump(notes_list, nf, indent=4)


def menu():
    flag = True

    while flag:
        print('\n---Notes Menu---\n')
        print('1.Show all notes')
        print('2.Search for a note')
        print('3.Add a note')
        print('4.Delete a note')
        print('5.Save and exit')

        user_input = input('Choose an option(1-5): ')

        if user_input == '1':
            show_notes()
        elif user_input == '2':
            search_note()
        elif user_input == '3':
            add_note()
        elif user_input == '4':
            delete_note()
        elif user_input == '5':
            save_notes()
            flag = False
        else:
            print('Enter a valid number.')


menu()
