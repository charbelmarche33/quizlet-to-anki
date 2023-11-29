import genanki
import time
from typing import Tuple, List


def make_apkg(card_tuple: Tuple[List, List]):
    """
    Makes anki cards from a tuple of 2 lists of front and backs of cards

    :param cards: Tuple of 2 lists that has strings for fronts of cards and strings for backs of cards in each respectively. Must be same length.
    :return: string of file name
    """
    my_deck = genanki.Deck(time.time_ns(), "Quizlet Imported Deck")
    fronts = card_tuple[0]
    backs = card_tuple[1]
    for front, back in zip(fronts, backs):
        my_note = genanki.Note(model=genanki.BASIC_MODEL, fields=[front, back])
        my_deck.add_note(my_note)
    file_name = str(time.time_ns()) + ".apkg"
    genanki.Package(my_deck).write_to_file(file_name)
    return file_name
