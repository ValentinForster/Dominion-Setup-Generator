import random
import copy

BASEGAME_CARDS = ['Bibliothek', 'Bürokrat', 'Burggraben', 'Banditin', 'Dorf', 'Händlerin', 'Garten',
                       'Geldverleiher', 'Hexe', 'Wilddiebin', 'Jahrmarkt', 'Vorbotin', 'Kapelle', 'Keller',
                       'Laboratorium', 'Markt', 'Miliz', 'Mine', 'Ratsversammlung', 'Schmiede', 'Vassal',
                       'Thronsaal', 'Umbau', 'Werkstatt', 'Wachposten', 'Töpferei']

INTRIGUE_CARDS = ["Burghof 👓", "Geheimkammer 👓", "Handlanger 👓", "Armenviertel 👓", "Große Halle 👓",
                  "Maskerade 👓", "Trickser 👓", "Verwalter 👓", "Wunschbrunnen 👓", "Baron 👓", "Bergwerk 👓",
                  "Brücke 👓", "Eisenhütte 👓", "Kupferschmiede 👓", "Späher 👓", "Verschwörer 👓", "Anbau 👓",
                  "Handelsposten 👓", "Herzog 👓", "Kerkermeister 👓", "Lakai 👓", "Saboteur 👓",
                  "Tribut 👓", "Adelige 👓", "Harem 👓"]

BOTH_COMBINED = BASEGAME_CARDS + INTRIGUE_CARDS

CHANGED_CARDS = ["Späher", "Herzog"] # Harem hinzufügen?

ATTACKS = ["Hexe", "Banditin", "Miliz", "Bürokrat", "Trickser 👓", "Kerkermeister 👓", "Lakai 👓", "Saboteur 👓"]
COST2_CARDS = ['Burggraben', 'Kapelle', 'Keller', "Burghof 👓", "Geheimkammer 👓", "Handlanger 👓", "Späher 👓"]
COST3_CARDS = ['Dorf', 'Händlerin', 'Vorbotin', 'Werkstatt', "Vassal", "Armenviertel 👓", "Große Halle 👓",
               "Maskerade 👓", "Verwalter 👓", "Wunschbrunnen 👓"]
COST4_CARDS = ['Garten', 'Geldverleiher', 'Schmiede', 'Thronsaal', 'Umbau', "Wilddiebin", "Baron 👓", "Bergwerk 👓",
               "Brücke 👓", "Eisenhütte 👓", "Kupferschmied 👓", "Verschwörer 👓", "Herzog 👓"]
COST5_plus_CARDS = ['Bibliothek', 'Jahrmarkt', 'Laboratorium', 'Markt', 'Mine', 'Ratsversammlung', "Wachposten",
                    "Töpferei", "Anbau 👓", "Handelsposten 👓",  "Tribut 👓", "Adelige 👓", "Harem 👓"]  # Harem weg?

ALL_TYPES = [ATTACKS, COST2_CARDS, COST3_CARDS, COST4_CARDS, COST5_plus_CARDS]

max_attacks = 2
max_cost2_cards = 2
max_cost3_cards = 3
max_cost4_cards = 2
max_cost5_plus_cards = 4

played_cards = []

card_counter = 0

def choose_cards():
    first_hands = random.randint(0, 100)
    if first_hands < 83:
        print('\x1b[6;97;40m' + 'Anfang: 4/3' + '\x1b[0m')
    else:
        print('\x1b[6;97;40m' + 'Anfang: 4/3' + '\x1b[0m')

    output = []
    copy_attacks = copy.copy(ATTACKS)
    copy_cost2_cards = copy.copy(COST2_CARDS)
    copy_cost3_cards = copy.copy(COST3_CARDS)
    copy_cost4_cards = copy.copy(COST4_CARDS)
    copy_cost5_plus_cards = copy.copy(COST5_plus_CARDS)
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
    for i in range(1, 11 - len(output)):
        choice = random.choice(copy_cost5_plus_cards)
        output.append(choice)
        copy_cost5_plus_cards.remove(choice)
    if len(output) < 10:
        supplement_list = [card for card in BOTH_COMBINED if card not in output]
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
        for card in kommt_weg:
            print('\x1b[6;30;41m' + "- " + card + " "*(18 - len(card)) + '\x1b[0m')
        for card in neu:
            print('\x1b[6;30;42m' + "+ " + card + " "*(18 - len(card)) + '\x1b[0m')
        for card in bleibt:
            print('\x1b[6;30;46m' + "= " + card + " "*(18 - len(card)) + '\x1b[0m')
        first_selection = list(new_selection)
        del new_selection



