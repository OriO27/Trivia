"""
OOrtiz 
16AUG20
V: 0.1
    Added Game Class
    Cookie Achievements
    Added Hint Mechanic
    Level 2
        TO DO:::
        Level 3
        Change question mechanic... Maybe
"""

class Game(object):
    def __init__(self):
        #initial methods
        self.PtS()
        self.Menu()

    def PtS(self):
        self.cookie = 0
        self.points = 0


    def Level1(self):
        lv1qA = [
            ["What is the last prime number encoutnered before reaching 100? ", 97, "Really?\nFine... I Guess..\nA prime number is only divisible by it-self and one."],
            ["What is seven times the number of planets in the inner solar system? ", 28, "\nInner planets are located before the asteroid beld...\nMercury, Venus, Earth, Mars...."],
            ["Why is six scared of seven?  (HINT: the answer is a three digit number) ", 789, "\nOkay, I admit it...\nthis one was just a mean question!\nBecause seven ate nine..Haha!\nFunny right?\nOh, don't think so? :("],
            ["What is the limit of e^(x) as x approaches negative infinity? ", 0, "\nHaven't take calculus yet?\nOr maybe it's been a while..\nOkay, if you answer this... you'll get it.\n1044 * 0"],
            ["What is the ninth number in the Fibonacci Sequence? ", 21, "\nThe next number in the Fibonacci Sequence is the sum of the previous two numbers.\nThe sequence starts with 0 and 1."]      
        ]
        #Level Instructions:
        print("\nLevel 1\n",
        "You will be given a series of 5 questions, answer them correctly to move on.\n",
        "HINT: ALL of the answers will be numeric.\n",
        "You will have three attempts at each question, fail to answer within that constraint and...\n you loose. :(!  \n\n")
        questions = 0
        restart = 0
        hint = 0
        lv1pass = False
        #Goes through question list.
        while questions <= 5:
            answers = input(lv1qA[questions][0])
            if answers.isdigit():
                answers = int(answers)
                #checks for correct answer.
                if answers == lv1qA[questions][1]:
                    print("Correct!")
                    questions += 1
                    restart = 0
                    self.points = 3 + (-1 * restart)
                
                #on three incorrect answers level exits
                else:
                    restart += 1
                    if restart == 3:
                        print("Disappointing.")
                        return lv1pass
                    print("Not quite...")
                        #HINT!!
            elif answers.upper() == 'HELP':
                print(lv1qA[questions][2])
                hint += 1

            else:
                print("I don't understand...")
            #if all questions are correct, returns a token for Level 2
            if questions == 5:
                lv1pass = True
                break

        if lv1pass == True:
            print("\n\nWell done!!")
            print("Pretty clever if I do say so myself!\nThat wasn't bad was it?")
            if hint == 0:
                print("And look at you! Didn't even use a single hint!")
                print("You get a virtual cookie!")
                self.cookie += 1
            print("Time for Level 2!")
        return lv1pass

    def Level2(self):
        print("\nLEVEL 2\n") 
        print("I hope you'll find this level far out!\n\nHeheh\nNow, lets start.")
        lv2qA = [
                ["What is the largest planet the outter solar system?\n1- Jupiter\n2-Saturn\n3-Uranus\n4-Neptune\n",1,"\nThey used to call him Zeus!"],
                ["The furthest man made object from earth is...\n1-Mariner 1\n2- Voyager 2\n3- Sputnik\n4-Voyager 1\n",4,"\nIt's been on a very lone long voyage!\n"],
                ["The total number of retired space shuttles...\n1-Two\n2-Three\n3-Four\n4-Five\n5-Six\n",3,"I think you can Google this one..."],
                ["There is liquid water on a body besides earth within our solar system.\n1-True\n2-False\n",1,"Fifty/Fifty chance.. No hint! :)"] ]
       
        #Level Instructions:
        print("\nLevel 1\n",
        "I got lazy and only wrote four questions.\n",
        "HINT: ALL of the answers will be numeric.\n",
        "You will have TWO attempts at each question, fail to answer within that constraint and...\n you loose. :(!  \n\n")
        questions = 0
        restart = 0
        hint = 0
        lv2pass = False
        #Goes through question list.
        while questions <= 4:
            answers = input(lv2qA[questions][0])
            if answers.isdigit():
                answers = int(answers)
                #checks for correct answer.
                if answers == lv2qA[questions][1]:
                    print("Correct!")
                    questions += 1
                    restart = 0
                    self.points = 3 + (-1 * restart)
                
                #on three incorrect answers level exits
                else:
                    restart += 1
                    if restart == 2:
                        print("Disappointing.")
                        return lv2pass
                    print("Not quite...")
            #HINT!!
            elif answers.upper() == 'HELP':
                print(lv2qA[questions][2])
                hint += 1

            else:
                print("I don't understand...")
            #if all questions are correct, returns a token for Level 2
            if questions == 4:
                lv2pass = True
                break

        if lv2pass == True:
            print("Excellent!")
            if hint == 0:
                print("And look at you! Didn't even use a single hint!")
                print("You get a virtual cookie!")
                self.cookie += 1
            print("Time for Level 3!")
            print("Once it's finished that is")        
        return lv2pass

    def RestartLevel(self, guide):
        if guide == False:
            Restart = False
            #Allows user to restart level or quit to main menu.
            while Restart == False:
                Play = str(input("Play again? "))
                if Play.upper() == ("yes").upper() or Play.upper() == ("y").upper() :
                    print("Not a quitter eh?\n")
                    Restart = True

                elif Play.upper() == ("no").upper() or Play.upper() == ('n').upper():
                    print("Till next time.\n")
                    Alive = False
                    return Alive
                else:
                    print("Unknown entry...\n")
            del guide
        elif guide == True:
            print("next")
            del guide


    def Play(self):
        Alive = True
        while Alive == True:
            #Level1
            guide = self.Level1()
            #executes if Level 1 is failed. 
            check = self.RestartLevel(guide)
            #checks to see if user wants to exit.
            if check == False:
                break
            #Level2
            guide = self.Level2()
            check = self.RestartLevel(guide)
            if check == False:
                break
            break

    def HighScores(self):
        print("No High Scores Yet!")

    def Tutorial(self):
        print("Who needs one?")
        print("\n")
        print("Well... If you must...")
        print("Type 'Help' at any time to get a hint about the level.")
        print("That should be enough of a tutorial!")

    def GoodBye(self):
        print("Goodbye")

    def Menu(self):
        quit = False
        while quit != True:
            print("\n\nSelect from the following options: \n")
            print("\n",\
                "|  1  |       Play        |\n",\
                "|  2  |    High Scores    |\n",\
                "|  3  |      Tutorial     |\n",\
                "|  4  |        Exit       |" )
            Select = input("   ")
            #If user inputs a correct digit, manu selection will appear. 
            if Select.isdigit():
                Select = int(Select)
                #Executes menu Entry
                if Select in range(1,5):
                    if Select == 1:
                        self.Play()
                    elif Select == 2:
                        self.HighScores()
                    elif Select == 3:
                        self.Tutorial()
                    elif Select == 4:
                        quit = True   
                else:
                    print("Unknown Entry.")    
            else:
                print("Unknown Entry.")

Game()