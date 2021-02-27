# Write your code here
import random

class Robot:
    def __init__(self,battery_level,heat,boredom,skills,name,rust):
        self.battery_level=battery_level
        self.heat=heat
        self.boredom=boredom
        self.skills=skills
        self.name=name
        self.rust=rust

    def charging(self):
        if(self.battery_level==100):
            print("{} is charged!".format(self.name))
        else:
            ba=self.battery_level
            h=self.heat
            b=self.boredom
            self.battery_level=min(self.battery_level+10,100)
            self.heat=max(self.heat-5,0)
            self.boredom=min(self.boredom+5,100)
            print("{}'s level of overheat was {}. Now it is {}.\n{}'s level of the battery was {}. Now it is {}.\n{}'s level of boredom was {}. Now it is {}.\n{} is recharged!".format(self.name,h,self.heat,self.name,ba,self.battery_level,self.name,b,self.boredom,self.name))

    def sleep(self):
        h=self.heat
        if(self.heat==0):
            print("{} is cool!".format(self.name))
        else:
            self.heat=max(0,self.heat-20)
            if(self.heat>0):
                print("{} cooled off!".format(self.name))
            print("{}'s level of overheat was {}. Now it is {}.".format(self.name,h,self.heat))
        if(self.heat==0):
            print("{} is cool!".format(self.name))

    def info(self):
        print("""{}'s stats are:
battery is {},
overheat is {},
skill level is {},
boredom is {},
rust is {}.""".format(self.name,self.battery_level,self.heat,self.skills,self.boredom,self.rust))

    def working(self):
        if(self.skills<50):
            print("{} has got to learn before working!".format(self.name))
        else:
            ba=self.battery_level
            b=self.boredom
            h=self.heat
            self.battery_level=max(0,self.battery_level-10)
            self.boredom=min(100,self.boredom+10)
            self.heat=min(100,self.heat+10)
            text=self.unlucky_event()
            print("{}'s level of boredom was {}. Now it is {}.\n{}'s level of overheat was {}. Now it is {}. \n{}'s level of the battery was {}. Now it is {}.".format(self.name,b,self.boredom,self.name,h,self.heat,self.name,ba,self.battery_level))
            if(text!=None):
                print(text)
            print("\n{} did well!".format(self.name))

    def learning(self):
        if(self.skills==100):
            print("There's nothing for {} to learn!".format(self.name))
        else:
            k=self.skills
            ba=self.battery_level
            h=self.heat
            b=self.boredom
            self.skills=min(self.skills+10,100)
            self.battery_level=max(self.battery_level-10,0)
            self.heat=min(self.heat+10,100)
            self.boredom=min(self.boredom+5,100)
            print("{}'s level of skill was {}. Now it is {}.\n{}'s level of overheat was {}. Now it is {}. \n{}'s level of the battery was {}. Now it is {}. \n{}'s level of boredom was {}. Now it is {}. \n{} has become smarter!".format(self.name,k,self.skills,self.name,h,self.heat,self.name,ba,self.battery_level,self.name,b,self.boredom,self.name))

    def oiling(self):
        r=self.rust
        if(self.rust==0):
            print("{} is fine, no need to oil!".format(self.name))
        else:
            self.rust=max(0,self.rust-20)
            print("{}'s level of rust was {}. Now it is {}. {} is less rusty!".format(self.name,r,self.rust,self.name))
        #if(self.heat==0):
        #    print("{} is cool!".format(self.name))

    def unlucky_event(self):
        events=['stepped into a puddle!',"encountered a sprinkler!","fell into the pool!"]
        damage=[10,30,50]
        chance=[0,1,1,1]
        if(random.choice(chance)==1):
            poz=random.choice(range(3))
            if(poz==0):
                print("Oh no, {} {}".format(self.name,events[poz]))
                r=self.rust
                self.rust=min(100,r+damage[poz])
            elif(poz==1):
                print("Oh, {} {}".format(self.name,events[poz]))
                r=self.rust
                self.rust=min(100,r+damage[poz])
            elif(poz==2):
                print("Guess what! {} {}".format(self.name,events[poz]))
                r=self.rust
                self.rust=min(100,r+damage[poz])
            print()
            return "{}'s level of rust was {}. Now it is {}.".format(self.name,r,self.rust)

    def play(self):
        b=self.boredom
        h=self.heat
        self.boredom=max(self.boredom-20,0)
        self.heat=min(self.heat+10,100)
        print(self.unlucky_event())
        print("{}'s level of overheat was {}. Now it is {}.\n{}'s level of boredom was {}. Now it is {}.".format(self.name,h,self.heat,self.name,b,self.boredom))
        if(self.boredom==0):
            print("\nDaneel is in a great mood")

def valid_command():
    valid_commands=["exit","play","info","recharge","sleep","work","learn","oil"]
    print("Choose:")
    command=input()
    if(command in valid_commands):
        return command
    else:
        print("Invalid input, try again!")

def valid_game():
    while(True):
        games=["Rock-paper-scissors","Numbers","rock-paper-scissors","numbers"]
        print("Which game would you like to play?")
        game_input=input()
        print()
        if(game_input in games):
            return game_input
        else:
            print("Please choose a valid option: Numbers or Rock-paper-scissors?")
            print()

def number_winner(first_entry,second_entry,goal,games_won,games_lost,draws):
    if(abs(goal-first_entry)>abs(goal-second_entry)):
        games_lost+=1
        print("The robot won!")
    elif(abs(goal-first_entry)<abs(goal-second_entry)):
        games_won+=1
        print("You won!")
    elif(abs(goal-first_entry)==abs(goal-second_entry)):
        draws+=1
        print("Draw!")
    print()
    return games_won,games_lost,draws

def rock_paper_winner(first_entry,second_entry,games_won,games_lost,draws):
    if(first_entry==second_entry):
        draws+=1
        print("It's a draw!")
    elif(first_entry=="rock"):
        if(second_entry=="scissors"):
            games_won+=1
            print("You won!")
        else:
            games_lost+=1
            print("Robot won!")
    elif(first_entry=="scissors"):
        if(second_entry=="paper"):
            games_won+=1
            print("You won!")
        else:
            games_lost+=1
            print("Robot won!")
    elif(first_entry=="paper"):
        if(second_entry=="rock"):
            games_won+=1
            print("You won!")
        else:
            games_lost+=1
            print("Robot won!")
    print()
    return games_won,games_lost,draws

def valid_int_input():
    while(True):
        print("What is your number?")
        valid_number=input()
        print()
        if(valid_number=="exit game"):
            return -1
        number_as_string=0
        for i in valid_number:
            if((i<'0' or i>'9') and i!='-'):
                number_as_string=1
                break
        if number_as_string==0:
            valid_number=int(valid_number)
            if(valid_number>1000000):
                print("Invalid input! The number can't be bigger than 1000000.")
            elif(valid_number<0):
                print("The number can't be negative!")
            else:
                return valid_number
        else:
            print("A string is not a valid input!")

def valid_move(possible_moves):
    while(True):
        print("What is your move?")
        move=input()
        print()
        if(move!='exit game'):
            if(move in possible_moves):
                return move
            else:
                print("No such option! Try again!")
                print()
        else:
            return move

def number_game():

    games_won=0
    games_lost=0
    draws=0

    while(True):
        humans_number=int(valid_int_input())

        if(humans_number==-1):
            break

        robot_number=random.choice(range(1000000))
        game_number=random.choice(range(1000000))

        print("The robot entered the number {}.\nThe goal number is {}.".format(robot_number,game_number))

        games_won,games_lost,draws=number_winner(humans_number,robot_number,game_number,games_won,games_lost,draws)

    print("You won: {},\nThe robot won: {},\nDraws: {}.".format(games_won,games_lost,draws))

def rock_paper_game():

    games_won=0
    games_lost=0
    draws=0

    moves=["rock","paper","scissors"]

    while(True):

        human_move=valid_move(moves)

        if(human_move=='exit game'):
            break

        robot_move=random.choice(moves)

        print("Robot chose {}".format(robot_move))

        games_won,games_lost,draws=rock_paper_winner(human_move,robot_move,games_won,games_lost,draws)

    print("You won: {},\nThe robot won: {},\nDraws: {}.".format(games_won,games_lost,draws))


def menu(Robot):
    print("""Available interactions with {}:
exit – Exit 
info – Check the vitals 
work – Work 
play – Play 
oil – Oil 
recharge – Recharge 
sleep – Sleep mode 
learn – Learn skills""".format(Robot.name))
    print()

print("How will you call your robot?")
Robopet=Robot(100,0,0,0,input(),0)
print()

while(True):
    menu(Robopet)
    chosen_command=valid_command()
    print()
    if(chosen_command=="exit"):
        print("Game over")
        break
    if(chosen_command=="play"):
        if(Robopet.battery_level>0):
            chosen_game=valid_game()
            if(chosen_game=="Numbers" or chosen_game=="numbers"):
                number_game()
            elif(chosen_game=="Rock-paper-scissors" or chosen_game=="rock-paper-scissors"):
                rock_paper_game()
            print()
            Robopet.play()
            print()
        else:
            print("The level of the battery is 0, {} needs recharging!".format(Robopet.name))
    if(chosen_command=="sleep"):
        if(Robopet.battery_level>0):
            Robopet.sleep()
            print()
        else:
            print("The level of the battery is 0, {} needs recharging!".format(Robopet.name))
    if(chosen_command=="recharge"):
            Robopet.charging()
            print()
    if(chosen_command=="work"):
        if(Robopet.battery_level>0):
            Robopet.working()
            print()
        else:
            print("The level of the battery is 0, {} needs recharging!".format(Robopet.name))
    if(chosen_command=="learn"):
        if(Robopet.battery_level>0):
            Robopet.learning()
            print()
        else:
            print("The level of the battery is 0, {} needs recharging!".format(Robopet.name))
    if(chosen_command=="oil"):
        if(Robopet.battery_level>0):
            Robopet.oiling()
            print()
        else:
            print("The level of the battery is 0, {} needs recharging!".format(Robopet.name))
    if(chosen_command=="info"):
        Robopet.info()
        print()
    if(Robopet.heat==100):
        print("The level of overheat reached 100, {} has blown up! Game over. Try again?".format(Robopet.name))
        break
    if(Robopet.rust==100):
        print("{} is too rusty! Game over. Try again?".format(Robopet.name))
        break
    if(Robopet.boredom==100):
        print("{} is too bored! {} needs to have fun! Game over".format(Robopet.name,Robopet.name))
        break
