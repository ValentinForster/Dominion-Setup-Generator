import random
import copy

basegame_cards_dict = {"Abenteurer": 4, "Bibliothek": 5, "Bürokrat": 4, "Burggraben": 2, "Dieb": 4, "Dorf": 3,
                  "Festmahl": 3, "Garten": 4, "Geldverleiher": 4, "Hexe": 5, "Holzfäller": 3, "Jahrmarkt": 5,
                  "Kanzler": 2, "Kapelle": 2, "Keller": 2, "Laboratorium": 5, "Markt": 5, "Miliz": 4, "Mine": 5,
                  "Ratsversammlung": 5, "Schmiede": 4, "Spion": 3, "Thronsaal": 4, "Umbau": 4, "Werkstatt": 3}

BASEGAME_CARDS = ['Abenteurer', 'Bibliothek', 'Bürokrat', 'Burggraben', 'Dieb', 'Dorf', 'Festmahl', 'Garten',
                       'Geldverleiher', 'Hexe', 'Holzfäller', 'Jahrmarkt', 'Kanzler', 'Kapelle', 'Keller',
                       'Laboratorium', 'Markt', 'Miliz', 'Mine', 'Ratsversammlung', 'Schmiede', 'Spion',
                       'Thronsaal', 'Umbau', 'Werkstatt']

INTRIGUE_CARDS = ["Burghof 👓", "Geheimkammer 👓", "Handlanger 👓", "Armenviertel 👓", "Große Halle 👓",
                  "Maskerade 👓", "Trickser 👓", "Verwalter 👓", "Wunschbrunnen 👓", "Baron 👓", "Bergwerk 👓",
                  "Brücke 👓", "Eisenhütte 👓", "Kupferschmiede 👓", "Späher 👓", "Verschwörer 👓", "Anbau 👓",
                  "Handelsposten 👓", "Herzog 👓", "Kerkermeister 👓", "Lakai 👓", "Saboteur 👓",
                  "Tribut 👓", "Adelige 👓", "Harem 👓"]

BOTH_COMBINED = BASEGAME_CARDS + INTRIGUE_CARDS

CHANGED_CARDS = ["Abenteurer", "Festmahl", "Kanzler", "Spion", "Späher", "Herzog"] # Harem hinzufügen?

ATTACKS = ["Hexe", "Dieb", "Miliz", "Spion", "Bürokrat", "Trickser 👓", "Kerkermeister 👓", "Lakai 👓", "Saboteur 👓"]
COST2_CARDS = ['Burggraben', 'Kanzler', 'Kapelle', 'Keller', "Burghof 👓", "Geheimkammer 👓", "Handlanger 👓",
               "Späher 👓"]
COST3_CARDS = ['Dorf', 'Festmahl', 'Holzfäller', 'Werkstatt', "Armenviertel 👓", "Große Halle 👓", "Maskerade 👓",
               "Verwalter 👓", "Wunschbrunnen 👓"]
COST4_CARDS = ['Abenteurer', 'Garten', 'Geldverleiher', 'Schmiede', 'Thronsaal', 'Umbau', "Baron", "Bergwerk 👓",
               "Brücke 👓", "Eisenhütte 👓", "Kupferschmied 👓", "Verschwörer 👓", "Herzog 👓"]
COST5_plus_CARDS = ['Bibliothek', 'Jahrmarkt', 'Laboratorium', 'Markt', 'Mine', 'Ratsversammlung', "Anbau 👓",
                    "Handelsposten 👓",  "Tribut 👓", "Adelige 👓", "Harem 👓"]  # Harem weg?

ALL_TYPES = [ATTACKS, COST2_CARDS, COST3_CARDS, COST4_CARDS, COST5_plus_CARDS]

max_attacks = 2
max_cost2_cards = 2
max_cost3_cards = 3
max_cost4_cards = 2
max_cost5_plus_cards = 4

played_cards = []

card_counter = 0

def choose_cards():
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
    for i in range(1, 10 - len(output)):
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
        print("")
        for card in kommt_weg:
            print('\x1b[6;30;41m' + "- " + card + " "*(18 - len(card)) + '\x1b[0m')
        for card in neu:
            print('\x1b[6;30;42m' + "+ " + card + " "*(18 - len(card)) + '\x1b[0m')
        for card in bleibt:
            print('\x1b[6;30;46m' + "= " + card + " "*(18 - len(card)) + '\x1b[0m')
        first_selection = list(new_selection)
        del new_selection
