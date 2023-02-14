import random
import copy

PLAYERS = ["Vali", "Andi", "Elli", "Grexi"]

basegame_cards_dict = {"Abenteurer": 4, "Bibliothek": 5, "Bürokrat": 4, "Burggraben": 2, "Dieb": 4, "Dorf": 3,
                  "Festmahl": 3, "Garten": 4, "Geldverleiher": 4, "Hexe": 5, "Holzfäller": 3, "Jahrmarkt": 5,
                  "Kanzler": 2, "Kapelle": 2, "Keller": 2, "Laboratorium": 5, "Markt": 5, "Miliz": 4, "Mine": 5,
                  "Ratsversammlung": 5, "Schmiede": 4, "Spion": 3, "Thronsaal": 4, "Umbau": 4, "Werkstatt": 3}

BASEGAME_CARDS = ['Abenteurer', 'Bibliothek', 'Bürokrat', 'Burggraben', 'Dieb', 'Dorf', 'Festmahl', 'Garten',
                       'Geldverleiher', 'Hexe', 'Holzfäller', 'Jahrmarkt', 'Kanzler', 'Kapelle', 'Keller',
                       'Laboratorium', 'Markt', 'Miliz', 'Mine', 'Ratsversammlung', 'Schmiede', 'Spion',
                       'Thronsaal', 'Umbau', 'Werkstatt']

CHANGED_CARDS = ["Abenteurer", "Festmahl", "Kanzler", "Spion"]

ATTACKS = ["Hexe", "Dieb", "Miliz", "Spion", "Bürokrat"]
COST2_CARDS = ['Burggraben', 'Kanzler', 'Kapelle', 'Keller']
COST3_CARDS = ['Dorf', 'Festmahl', 'Holzfäller', 'Werkstatt']
COST4_CARDS = ['Abenteurer', 'Garten', 'Geldverleiher', 'Schmiede', 'Thronsaal', 'Umbau']
COST5_CARDS = ['Bibliothek', 'Jahrmarkt', 'Laboratorium', 'Markt', 'Mine', 'Ratsversammlung']
ALL_TYPES = [ATTACKS, COST2_CARDS, COST3_CARDS, COST4_CARDS, COST5_CARDS]

max_attacks = 2
max_cost2_cards = 2
max_cost3_cards = 3
max_cost4_cards = 2
max_cost5_cards = 4

played_cards = []

card_counter = 0

def choose_cards():
    output = []
    copy_attacks = copy.copy(ATTACKS)
    copy_cost2_cards = copy.copy(COST2_CARDS)
    copy_cost3_cards = copy.copy(COST3_CARDS)
    copy_cost4_cards = copy.copy(COST4_CARDS)
    copy_cost5_cards = copy.copy(COST5_CARDS)
    for i in range(0, max_attacks):
        choice = random.choice(copy_attacks)
        output.append(choice)
        copy_attacks.remove(choice)
    for i in range(0, max_cost2_cards):
        choice = random.choice(copy_cost2_cards)
        output.append(choice)
        copy_cost2_cards.remove(choice)
    for i in range(0, max_cost3_cards):
        choice = random.choice(copy_cost3_cards)
        output.append(choice)
        copy_cost3_cards.remove(choice)
    for i in range(0, max_cost4_cards):
        choice = random.choice(copy_cost4_cards)
        output.append(choice)
        copy_cost4_cards.remove(choice)
    for i in range(1, 10 - len(output)):
        choice = random.choice(copy_cost5_cards)
        output.append(choice)
        copy_cost5_cards.remove(choice)
    if len(output) < 10:
        supplement_list = [card for card in BASEGAME_CARDS if card not in output]
        for i in range(0, 10 - len(output)):
            output.append(random.choice(supplement_list))
    return output

first_selection = choose_cards()
for card in first_selection:
    print(card)

while True:
    print("")
    user_input = input("Noch eine Runde?")
    if user_input == "":
        new_selection = choose_cards()
        bleibt = [card for card in new_selection if card in first_selection]
        kommt_weg = [card for card in first_selection if card not in new_selection]
        neu = [card for card in new_selection if card not in first_selection]
        print("")
        for card in kommt_weg:
            print('\x1b[6;30;41m' + "- " + card + " "*(15 - len(card) + 2) + '\x1b[0m')
        for card in neu:
            print('\x1b[6;30;42m' + "+ " + card + " "*(15 - len(card) + 2) + '\x1b[0m')
        for card in bleibt:
            print('\x1b[6;30;44m' + "= " + card + " "*(15 - len(card) + 2) + '\x1b[0m')
        first_selection = list(new_selection)
        del new_selection
