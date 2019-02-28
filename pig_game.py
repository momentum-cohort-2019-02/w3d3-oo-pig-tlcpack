import random


class HumanPlayer():
    """Creating the human player for Pig game"""
    
    def __init__(self):
        # self.roll_choice = roll_choice
        # self.die_roll = die_roll
        # self.rolls_this_turn = rolls_this_turn
        # self.current_turn_score = current_turn_score
        # self.overall_score = 0
        # self.computer_score = computer_score

        def roll_choice(self):
            """User chooses if they want to roll"""
            self.roll_choice = input("Would you like to roll the dice? (y/n): ")
            return self.roll_choice

    def roll_die(self, roll_choice):
        """User rolls dice"""
        if roll_choice == 'y':   
            self.die_roll = random.randint(0,6)
            print(die_roll)
            self.rolls_this_turn += 1
            print(self.rolls_this_turn)
            return self.die_roll
        else:
            self.overall_score += self.current_turn_score
            print(self.overall_score)
            return self.overall_score   

    
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

## not using die here, thought I would need it during original design
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
    def __init__(self):
        # self.roll_choice = roll_choice
        # self.die_roll = die_roll
        # self.rolls_this_turn = rolls_this_turn
        # self.current_turn_score = current_turn_score
        # self.overall_score = overall_score
        # self.computer_score = computer_score

        def roll_die(self):
            """Computer rolls dice"""
            while current_turn_score < 20:   
                self.die_roll = random.randint(0,6)
                print(self.die_roll)
                self.rolls_this_turn += 1
                print(self.rolls_this_turn)
                self.current_turn_score += self.die_roll
                print(self.current_turn_score)
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
    """creating the game"""

    def __init__(self, human_player, computer_player):
        self.human_player = human_player
        self.computer_player = computer_player
        self.human_total_score = 0
        self.computer_total_score = 0
        self.roll_die = random.randint(0,6)

    def run_game(self):
        # computer_score = self.computer_player.current_turn_score(self.roll_die)
        # self.computer_total_score += computer_score
        # human_score = self.human_player.current_turn_score(self.roll_die)
        # self.human_total_score += human_score

        roll_choice = ''
        while True:
            roll_choice = input("Would you like to roll? (y/n): ")
            if roll_choice == 'n':
                self.human_player.overall_score(self.human_total_score, self.human_player.current_turn_score)
                break
            else:
                current_roll = self.roll_die
                print(current_roll)
                if current_roll == 1:
                    self.human_player.current_turn_score == 0
                    break
                else:
                    self.human_player.current_turn_score(current_roll)

        while True:
            current_roll = self.roll_die
            if current_roll == 1:
                self.computer_player.current_turn_score == 0
                break
            elif self.computer_player.current_turn_score >= 20:
                self.computer_player.overall_score(self.computer_total_score, self.computer_player.current_turn_score)
                break
            else:
                self.computer_player.current_turn_score(current_roll)

        while self.human_total_score >= 100 or self.computer_total_score >= 100:
            



            if self.human_total_score >= 100:
                print("The human wins!")
            if self.computer_total_score >= 100:
                print("The computer wins!")


if __name__ == "__main__":
    
    p1 = HumanPlayer()
    p2 = ComPlayer()
    

    game = Game(p1, p2)
    game.run_game()


