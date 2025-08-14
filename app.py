import json
import os
from pathlib import Path

FILE_NOTE = 'notes.json'


def load_notes():
    pass


def show_notes():
    pass


def search_note():
    pass


def add_note():
    pass


def delete_note():
    pass


def save_notes():
    pass


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
