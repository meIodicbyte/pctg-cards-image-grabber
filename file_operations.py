import os
import csv
import requests
import logging
import re

def get_cards_from_csv(file_path):

    logging.basicConfig(
        filename='csv_processing.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    cards = []

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)

        deck_name = next(reader)[0]
        logging.info(f"Processing deck:{deck_name}")

        for row in reader:
            if len(row) == 3:
                card_name = row[0]
                print_number = row[1] if is_valid_print_number(row[1]) else None
                quantity = row[2]
        

        cards.append((card_name, print_number, quantity))

def is_valid_print_number(print_number):
    #Validates if the print number is in the correct format (e.g., 20/150)
    return bool(re.match(r'^\d+/\d+$', print_number))

if __name__ == "__main__":
    decklist_path = "decklist.csv"

    if os.path.exists(decklist_path):
        cards =  get_cards_from_csv(decklist_path)
        logging.info(f"Total cards processed: {len(cards)}")
    else:
        logging.error(f"decklist.csv not found. No list was processed.")
