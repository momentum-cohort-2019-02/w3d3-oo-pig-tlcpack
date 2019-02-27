import random


class HumanPlayer():
    """Creating the human player for Pig game"""
    # i think this may be too many attributes for init statement
    def __init__(self, overall_score):
        # self.roll_choice = roll_choice
        # self.die_roll = die_roll
        # self.rolls_this_turn = rolls_this_turn
        # self.current_turn_score = current_turn_score
        self.overall_score = overall_score
        # self.computer_score = computer_score

    def roll_choice(self):
        """User chooses if they want to roll"""
        self.roll_choice = input("Would you like to roll the dice? (y/n): ")
        return self.roll_choice

    def roll_die(self, roll_choice):
        """User rolls dice"""
        if roll_choice = 'y':   
            self.die_roll = random.randint(0,6)
            print(die_roll)
            self.rolls_this_turn += 1
            print(self.rolls_this_turn)
            return self.die_roll

    
    def current_turn_score(self, die_roll):
        """Adding dice roll score to current turn score"""
        self.current_turn_score = 0
        self.current_turn_score += die_roll
        return self.current_turn_score
    
    def overall_score(self, runnning_score, current_turn_score):
        """Adding turn score to overall score"""
        self.overall_score += self.current_turn_score
        print(self.overall_score)
        return self.overall_score

class Die():
    """Creating the die"""

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        self.die_roll = random.randint(0,self.sides)
        return self.die_roll

class ComPlayer():
    """Creating the computer player for Pig game"""

    # i think this may be too many attributes for init statement
    def __init__(self, overall_score):
        # self.roll_choice = roll_choice
        # self.die_roll = die_roll
        # self.rolls_this_turn = rolls_this_turn
        # self.current_turn_score = current_turn_score
        self.overall_score = overall_score
        # self.computer_score = computer_score

    def roll_dice(self, roll_choice):
        """User rolls dice"""
        if current_turn_score < 20:   
            self.die_roll = random.randint(0,6)
            print(die_roll)
            self.rolls_this_turn += 1
            print(self.rolls_this_turn)
            return self.die_roll

    
    def current_turn_score(self, die_roll):
        """Adding dice roll score to current turn score"""
        self.current_turn_score = 0
        self.current_turn_score += die_roll
        return self.current_turn_score
    
    def overall_score(self, runnning_score, current_turn_score):
        """Adding turn score to overall score"""
        self.overall_score += self.current_turn_score
        print(self.overall_score)
        return self.overall_score

class Game():


