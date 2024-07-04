import random
from helpers import get_file_path

class DiceQuantity:
    def __init__(self, value: int):
        if value < 1:
            raise ValueError("Dice quantity must be greater than 0")
        if not isinstance(value, int):
            raise TypeError("Dice quantity value must be an integer")
        self.value = value

class DiceSideQuantity:
    def __init__(self, value: int):
        if value < 2:
            raise ValueError("Dice must have more than 1 side")
        if not isinstance(value, int):
            raise TypeError("Number of dice sides must be an integer")
        self.value = value

def roll(dice_qty: DiceQuantity, dice_sides: DiceSideQuantity) -> int:
    """
    Roll a specified quantity of dice with a specfied number of sides using true randomness and a normal distribution.

    Args:
        dice_qty (DiceQuantity): The quantity of dice to roll (must be greater than 0).
        dice_sides (DiceSideQuantity): The number of sides on each die (must be greater than 1).

    Returns:
        int: The sum of the dice rolls.

    Raises:
        TypeError: If the dice_qty is not an instance of DiceQuantity or dice_sides is not an instance of DiceSideQuantity.
    """
    
    if not isinstance(dice_qty, DiceQuantity):
        raise TypeError("The dice_qty must be an instance of DiceQuantity")
    if not isinstance(dice_sides, DiceSideQuantity):
        raise TypeError("The dice_sides must be an instance of DiceSidesQuantity")

    random_device = random.SystemRandom()

    return sum(random_device.randint(1, dice_sides.value) for _ in range(dice_qty.value))

def load_file_lines(file_path: str) -> list:
    """
    Extracts lines from a file putting each line into a list.

    Args:
        file_path (str): The path to the file.

    Returns:
        list: A list of names.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: For other unexpected file handling errors.
    """

    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file at {file_path} does not exist.") from e
    except OSError as e:
        raise OSError(f"An error occured while reading the file at {file_path}: {e}") from e

# Ship name generation

ship_first_name_file = get_file_path('data/ship_first_names.txt')
ship_second_name_file = get_file_path('data/ship_second_names.txt')

ship_first_names = load_file_lines(ship_first_name_file)
ship_second_names = load_file_lines(ship_second_name_file)

def generate_ship_name() -> str:
    """
    Generates random ship name by combining two randomly selected names.

    Returns:
        str: A randomly generated ship name.

    Raises:
        IndexError: If indices are less than 0 or greater than last index
    """
    dice_qty = DiceQuantity(1)
    dice_sides_first = DiceSideQuantity(len(ship_first_names))
    dice_sides_second = DiceSideQuantity(len(ship_second_names))

    first_index = roll(dice_qty, dice_sides_first) - 1
    second_index = roll(dice_qty, dice_sides_second) - 1

    if first_index < 0:
        raise IndexError(f"First Index is less than 0 with a value of {first_index}")
    if second_index < 0:
        raise IndexError(f"Second Index is less than 0 with a value of {second_index}")

    return f"{ship_first_names[first_index]} {ship_second_names[second_index]}"

# Generate and print random ship names
if __name__ == "__main__":
    for _ in range(10):
        print(generate_ship_name())
