"""Exercise 1: Menu filtering.

Load data/menu.json and print every AVAILABLE item under $10.00,
sorted by price, cheapest first.

Expected output shape:
    Green Tea            $3.25
    Iced Coffee          $4.25
    ...

Requirements:
  - use an f-string for the output
  - type-hint every function you write
"""

import json
from pathlib import Path

MENU_PATH = Path(__file__).parent / "data" / "menu.json"


def load_menu() -> list[dict]:
    """Read the menu file and return it as a list of dictionaries."""
    with MENU_PATH.open() as f:
        return json.load(f)


def available_under(menu: list[dict], limit: float) -> list[dict]:
    """Return available items priced below `limit`, sorted cheapest first."""
    # TODO: filter items priced under $10, then sort by price.
    filtered_list: list[dict] = [i for i in menu if i["available"] and i["price"] < limit]
    sorted_list: list[dict] = sorted(filtered_list, key=lambda x: x["price"]) # lambda is just a temporary function
    return sorted_list


def main() -> None:
    menu = load_menu()
    for item in available_under(menu, 10.00):
        # TODO: print name and price using an f-string.
        print(f"{item['name']:<20} ${item['price']:.2f}")
        # Hint: f"{item['name']:<20} ${item['price']:.2f}" # <20 = left-align the value in a field 
        #20 characters wide; extra spaces are added after shorter names so the next column lines up


if __name__ == "__main__":
    main()
