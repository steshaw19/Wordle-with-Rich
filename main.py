from rich.console import Console
from random import choice
from words import word_list

welcome_message = f'\n[white on blue] WELCOME TO WORDLE [/]\n'
player_instructions = 'You may start guessing.\n'
allowed_guesses = 6

def correct_guess(letter):
    return f'[black on green]{letter}[/]'

def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'

def incorrect_guess(letter):
    return f'[black on white]{letter}[/]'

if __name__ == '__main__':
    console = Console()
    chosen_word = choice(word_list)
    console.print(welcome_message)
    console.print(player_instructions)