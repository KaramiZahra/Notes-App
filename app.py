import json
import os
from pathlib import Path
import uuid
from datetime import datetime

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
    if notes_list:
        for index, note in enumerate(notes_list, start=1):
            print(
                f"\n{index}.{note['title']} → {note['content']} \nCreated at: {note['created_at'][:16].replace('T', ' ')}")
    else:
        print('You have no notes.')


def search_note():
    query = input('Search: ').strip()
    search_results = []
    if query:
        for note in notes_list:
            if query.lower() in note['title'].lower() or query.lower() in note['content'].lower():
                search_results.append(note)
        if search_results:
            print('\nNote(s) found:')
            for index, result in enumerate(search_results, start=1):
                print(f"{index}.{result['title']} → {result['content']}")
        else:
            print('Note not found.')
    else:
        print('Search can\'t be empty.')


def add_note():
    new_note_title = input('Enter the title of your note: ').strip()
    new_note_content = input('Enter the content of your note: ').strip()
    if new_note_title and new_note_content and all(note['title'] != new_note_title for note in notes_list):
        new_note = {
            'id': str(uuid.uuid4()),
            'title': new_note_title,
            'content': new_note_content,
            'created_at': datetime.now().isoformat()
        }
        notes_list.append(new_note)
        print('Note successfully added.')
    else:
        print('Note can\'t be empty or repetitious.')


def delete_note():
    show_notes()
    try:
        rm_note = int(input('Enter note number to delete: '))
    except ValueError:
        print('Note doesn\'t exist')
        return

    if 1 <= rm_note <= len(notes_list):
        del notes_list[rm_note - 1]
        print('Note successfully deleted.')
    else:
        print('Note doesn\'t exist')


def edit_note():
    show_notes()
    try:
        edit_note = int(input('Enter note number to edit: '))
    except ValueError:
        print('Note doesn\'t exist')
        return
    if 1 <= edit_note <= len(notes_list):
        selected_note = notes_list[edit_note - 1]
        new_title = input('Enter your new title: ').strip()
        new_content = input('Enter your new content: ').strip()
        if new_title and new_content:
            selected_note['title'] = new_title
            selected_note['content'] = new_content
            print('Note successfully edited.')
        else:
            print('Note can\'t be empty.')
    else:
        print('Note doesn\'t exist')


def reorder_notes():
    show_notes()
    try:
        prev_pos = int(input('Enter note number to move: '))
        new_pos = int(
            input(f"Enter the new position(1-{len(notes_list)}): "))
    except ValueError:
        print('Note doesn\'t exist')
        return
    if prev_pos in range(1, len(notes_list)+1) and new_pos in range(1, len(notes_list)+1):
        note_to_move = notes_list.pop(prev_pos - 1)
        notes_list.insert(new_pos - 1, note_to_move)
        print('Note successfully reordered.')
    else:
        print('Enter a valid number.')


def sort_notes():
    sort_type = input('Enter 1 to sort by date and 2 to sort by title: ')
    if sort_type == '1':
        sorted_dates = sorted(notes_list, key=lambda note: note['created_at'])
        for index, note in enumerate(sorted_dates, start=1):
            print(
                f"\n{index}.{note['title']} → {note['content']} \nCreated at: {note['created_at'][:16].replace('T', ' ')}")
    elif sort_type == '2':
        sorted_title = sorted(notes_list, key=lambda note: note['title'])
        for index, note in enumerate(sorted_title, start=1):
            print(
                f"\n{index}.{note['title']} → {note['content']} \nCreated at: {note['created_at'][:16].replace('T', ' ')}")
    else:
        print('Enter a valid number.')


def save_notes():
    with open(FILE_NOTE, 'w') as nf:
        json.dump(notes_list, nf, indent=4)


def menu():
    flag = True

    while flag:
        print('\n---Notes Menu---\n')
        print('1.Show all notes')
        print('2.Search a note')
        print('3.Add a note')
        print('4.Delete a note')
        print('5.Edit a note')
        print('6.Reorder notes')
        print('7.Sort notes')
        print('8.Save and exit')

        user_input = input('Choose an option(1-8): ')

        if user_input == '1':
            show_notes()
        elif user_input == '2':
            search_note()
        elif user_input == '3':
            add_note()
        elif user_input == '4':
            delete_note()
        elif user_input == '5':
            edit_note()
        elif user_input == '6':
            reorder_notes()
        elif user_input == '7':
            sort_notes()
        elif user_input == '8':
            save_notes()
            flag = False
        else:
            print('Enter a valid number.')


menu()
