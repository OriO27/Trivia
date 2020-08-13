"""
OOrtiz 
12MAY20
"""





def Level1():
    lv1qA = [
        ["What is the last prime number encoutnered before reaching 100? ", 97],
        ["What is seven times the number of planets in the inner solar system? ", 28],
        ["Why is six scared of seven?  (HINT: the answer is numeric) ", 789],
        ["What is the limit of e^(x) as x approaches negative infinity? ", 0],
        ["What is the ninth number in the Fibonacci Sequence? ", 21]      
    ]
    #Level Instructions:
    print("\nLevel 1\n",
    "You will be given a series of 5 questions, answer them correctly to move on.\n",
    "HINT: ALL of the answers will be numeric.\n",
    "You will have three attempts at each question, fail to answer you loose.\n\n")
    questions = 0
    restart = 0
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
            #on three incorrect answers level exits
            else:
                restart += 1
                if restart == 3:
                    print("Disappointing.")
                    return lv1pass
                print("Not quite...")
        else:
            print("I don't understand...")
        #if all questions are correct, returns a token for Level 2
        if questions == 5:
            lv1pass = True
            return lv1pass
    if lv1pass == True:
        print("Well done, that wasn't bad was it?\n","Time for Level 2.")
    return lv1pass

def Level2():
    print("\nLEVEL 2\n") 
    print("Select the best response to the following situations.")
    lv2qA = [
            ["Before an exam is it better to: \nTake a nap or shake violently"]
            ["What is the largest small ant?"]
            ["Peter pondered perfusely, perhabs Paul pillaged "]

    ]
    lv2pass = False
    return lv2pass

def RestartLevel(guide):
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


def Play():
    Alive = True
    while Alive == True:
        #Level1
        guide = Level1()
        #executes if Level 1 is failed. 
        check = RestartLevel(guide)
        #checks to see if user wants to exit.
        if check == False:
            break
        #Level2
        guide = Level2()
        check = RestartLevel(guide)
        if check == False:
            break

def HighScores():
    print("No High Scores Yet!")

def Tutorial():
    print("Who needs one?")

def GoodBye():
    print

def Menu():
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
                    Play()
                elif Select == 2:
                    HighScores()
                elif Select == 3:
                    Tutorial()
                elif Select == 4:
                    quit = True   
            else:
                print("Unknown Entry.")    
        else:
            print("Unknown Entry.")

Menu()