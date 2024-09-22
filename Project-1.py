import random

def roll_dice(sides=6):
    """
    Simulate rolling a dice with a specified number of sides.
    Default is a 6-sided dice.
    """
    return random.randint(1, sides)

def main():
    print("Welcome to the Dice Roller Simulator!")
    while True:
        # Ask the user how many sides their dice has
        sides = input("Enter the number of sides for the dice (default is 6): ")
        
        # Use default 6 sides if input is blank
        if sides == "":
            sides = 6
        else:
            sides = int(sides)
        
        # Roll the dice
        result = roll_dice(sides)
        print(f"\nYou rolled a {result} on a {sides}-sided dice.")
        
        # Ask the user if they want to roll again
        roll_again = input("\nDo you want to roll again? (yes/no): ").lower()
        if roll_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
