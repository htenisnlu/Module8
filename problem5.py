# Hikmet Tenis
# 08/23/2024
# This function that checks whether your game character has picked up all the items needed to perform 
# certain tasks and checks against any status debuffs. Confirm checks with print statements.

class Character:
    def __init__(self, nickname, weapons, weaknesses):
        # Initialize the character with a nickname, a list of weapons, and a list of weaknesses
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def check_tasks(self):
        # Define the required items for each task
        task_1_items = {'rope', 'coat', 'first aid kit'}
        task_2_items = {'pan', 'groceries'}
        task_3_items = {'pen', 'paper', 'idea'}

        # Check if the character has the 'slow' debuff
        has_slow_debuff = 'slow' in self.weaknesses

        # Task 1: Climb a mountain - needs rope, coat, and first aid kit, cannot have slow
        if task_1_items.issubset(self.weapons) and not has_slow_debuff:
            print("Character can climb the mountain.")
        else:
            print("Character cannot climb the mountain.")

        # Task 2: Cook a meal - needs pan, groceries, cannot have slow
        if task_2_items.issubset(self.weapons) and not has_slow_debuff:
            print("Character can cook a meal.")
        else:
            print("Character cannot cook a meal.")

        # Task 3: Write a book - needs pen, paper, idea, cannot have confusion
        if task_3_items.issubset(self.weapons) and 'confusion' not in self.weaknesses:
            print("Character can write a book.")
        else:
            print("Character cannot write a book.")

# Example Usage
# Create a character with a nickname, a list of weapons, and a list of weaknesses
player1 = Character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])

# Check if the character can perform the tasks
player1.check_tasks()
