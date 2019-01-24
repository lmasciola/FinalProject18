import sys

clues = []
#this is the list of clues the player will use to help them solve the mystery

quotes = []
#this is the list of funny quotes the player may discover during the episode

possible_murderers = ["suicide"]
#this is the list of possible ways the Jennifer Wilson died

friendship_lestrade = 3
#this variable measures your friendship level with Lestrade and will be altered based on decisions made during the games

def x():
    """Players will be able to read text one line at a time and press enter to read the next line of text. The player will also be able to type the word 'clues' or 'quotes' to see the list of clues or quotes they have so far."""
    x = input("<")
    #this takes the user's input after they read each line of text
    x_options = ["", "clues", "quotes"]
    #this is the list of options for the variable x
    while x.lower() not in x_options:
        #this while loop will continue to ask the user for a valid input to x if their input is not in the x_options list
        x = input("<")
    if x == "":
        #if the user input to x is "", the next line of text will print
        return x
    elif x.lower() == "clues":
        #if the user input to x is "clues", the list of clues will print
        print(f"The clues you have discovered so far are:")
        print(*clues, sep = "\n")
        return
    elif x.lower() == "quotes":
        #if the user input to x is "quotes", the list of quotes will print
        print(f"The quotes you have discovered so far are:")
        print(*quotes, sep = "\n")
        return

def murderer():
    """This function will ask the player if they think they know who the murderer is"""
    murderer = input("Based on the information you have, do you think you know who the murderer is? If you chose wrong, the game will end. Enter: 'y' or 'n'.")
    #this takes the user's input to the above question
    options = ["yes", "y", "no", "n"]
    #this is the list of options for the variable murder
    while murderer.lower() not in options:
        #this while loop will continue to ask the user for a valid input to murderer if their input is not in the options list
        murderer = input("Based on the information you have, do you think you know who the murderer is? If you chose wrong, the game will end. Enter: 'y' or 'n'.")
    if murderer.lower() == "yes" or murderer.lower() == "y":
        #if the user input to murderer is "y" or "yes", the possible murderers list will be printed and the user will be prompted with another question
        print(f"These are the possible murderers so far: {', '.join(possible_murderers)}")
        murderer_1 = input("Who do you think killed the victim?")
        #this input will ask the user's input the above question
        while murderer_1 not in possible_murderers:
            #this while loop will continue to ask the user for a valid input to murderer_1 if their input is not in the possible_murderers list
            murderer_1 = input("Who do you think killed the victim?")
        if murderer_1.lower() == "suicide":
            #if the user's input to murderer_1 is "suicide", the following will print
            print("You had already said that it couldn't have been a suicide, but you have changed your mind.")
            x()
            print("In the coming months, 5 more 'suicides' appear in the newspapers. The police are out of their depth. You now definitey think that they weren't suicides. But it's too late. Even if you are able to find the killer, 5 more lives have been lost because of your misjudgement.")
            x()
            restart = input("Would you like to go back to the crime scene and restart? Enter: 'y' or 'n'.")
            #this variable will take the user's input to the above question
            while restart.lower() not in ["yes", "y", "no", "n"]:
                #this while loop will continue to ask the user for a valid input to restart if their input is not in the above list
                restart = input("Would you like to go back to the crime scene and restart? Enter: 'y' or 'n'.")
            if restart.lower() in ["yes", "y"]:
                #if the user's input to restart is "yes" or "y", the scene_5() function is called
                scene_5()
            elif restart.lower() in ["no", "n"]:
                #if the user's input to restart is "no" or "n", the following will be print and the game will end (using sys.exit())
                print("Goodbye.")
                sys.exit()
        elif murderer_1.lower() == "husband":
            #if the input to murder_1 is "husband", the following will print
            print("You believe the murderer to be the husband. However, when he was told of Jennifer Wilson's death, he was extremely distraught and had an alibi.")
            x()
            print("After you confronted the husband and realized he was not the murderer, you returned to London, but were unable to find the murderer.")
            x()
            print("In the coming months, 5 more 'suicides' appear in the newspapers. The police are out of their depth. You now definitey think that they weren't suicides. But it's too late. Even if you are able to find the killer, 5 more lives have been lost because of your misjudgement.")
            x()
            restart = input("Would you like to go back to the crime scene and restart? Enter: 'y' or 'n'.")
            #this variable will take the user's input to the above question
            while restart.lower() not in ["yes", "y", "no", "n"]:
                #this while loop will continue to ask the user for a valid input to restart if their input is not in the above list
                restart = input("Would you like to go back to the crime scene and restart? Enter: 'y' or 'n'.")
            if restart.lower() in ["yes", "y"]:
                #if the user's input to restart is "yes" or "y", the scene_5() function is called
                scene_5()
            elif restart.lower() in ["no", "n"]:
                #if the user's input to restart is "no" or "n", the following will be print and the game will end (using sys.exit())
                print("Goodbye.")
                sys.exit()
        elif murderer_1.lower() == "lover":
            #if the input to murder_1 is "lover", the following will print
            print("You believe the murderer to be the lover.")
            x()
            print("You searched for days through Jennifer Wilson's bag and other items, but were unable to identify her possible lover(s)")
            x()
            print("Time was wasted looking for the lover in hopes of questioning them.")
            x()
            print("In the coming months, 5 more 'suicides' appear in the newspapers. The police are out of their depth. You now definitey think that they weren't suicides. But it's too late. Even if you are able to find the killer, 5 more lives have been lost because of your misjudgement.")
            x()
            restart = input("Would you like to go back to the crime scene and restart? Enter: 'y' or 'n'.")
            #this variable will take the user's input to the above question
            while restart.lower() not in ["yes", "y", "no", "n"]:
                #this while loop will continue to ask the user for a valid input to restart if their input is not in the above list
                restart = input("Would you like to go back to the crime scene and restart? Enter: 'y' or 'n'.")
            if restart.lower() in ["yes", "y"]:
                #if the user's input to restart is "yes" or "y", the scene_5() function is called
                scene_5()
            elif restart.lower() in ["no", "n"]:
                #if the user's input to restart is "no" or "n", the following will be print and the game will end (using sys.exit())
                print("Goodbye.")
                sys.exit()
        elif murderer_1.lower() == "taxi driver":
            #if the input to murder_1 is "taxi driver", the following will print and the game will end
            print("JOHN: Sherlock, you okay?")
            x()
            print("YOU: What? Yes, yes.")
            x()
            print("You receive a text from Jennifer Wilson's phone that says 'COME WITH ME'")
            x()
            print("JOHN: So how can the phone be here?")
            x()
            print("YOU: I don’t know ...")
            x()
            print("JOHN: I’ll phone it again.")
            x()
            print("YOU (putting on your coat and heading out the door): Good idea.")
            x()
            print("JOHN: Where are you going?")
            x()
            print("YOU: Nowhere. Fresh air, just popping out for a moment.")
            x()
            print("JOHN: You sure you’re all right?")
            x()
            print("YOU: I’m fine!")
            x()
            print("You head outside of your flat. It is currently dark out. You are alone on the street beside the taxi is waiting for you.")
            x()
            print("TAXI DRIVER: Taxi for Sherlock Holmes.")
            x()
            print("YOU: I didn’t order a taxi.")
            x()
            print("TAXI DRIVER: Doesn’t mean you don’t need one.")
            x()
            print("YOU: You’re the cabbie - the one who stopped outside Northumberland Street. It was you, not your passenger.")
            x()
            print("TAXI DRIVER: You see, no one ever thinks about the cabbie. It’s like we’re invisible. Just the back of a head. Proper advantage for a serial killer.")
            x()
            print("YOU: Is this a confession?")
            x()
            print("TAXI DRIVER: Oh, yes. And I’ll tell you what else - if you go and get the coppers now, I won’t run, I’ll sit quiet and they can take me down. I promise.")
            x()
            print("YOU: Why?")
            x()
            print("TAXI DRIVER: Because you’re not going to do that.")
            x()
            print("You went with the cabbie driver. He took you to a college that was closed and just talked to you. Eventually, John found you and brought the police to your location. When the police arrived, the taxi driver was dead. However, the driver told you why he did what he did and that he did this because somebody wanted to catch your attention. More importantly, he told you he did it for...")
            x()
            print("...")
            x()
            print("...")
            x()
            print("...Moriarty.")
        elif murderer_1.lower() == "mrs. hudson":
            #the following prints
            print("Are you serious? That little old lady? A murderer? No. You're done. Goodbye.")
            x()
            sys.exit()
        elif murderer_1.lower() == "lestrade":
            #the follwoing prints
            print("Okay. No. It would be an interesting cover, but no.")
            x()
            restart = input("Would you like to go back to the crime scene and restart? Enter: 'y' or 'n'.")
            #this variable will take the user's input to the above question
            while restart.lower() not in ["yes", "y", "no", "n"]:
                #this while loop will continue to ask the user for a valid input to restart if their input is not in the above list
                restart = input("Would you like to go back to the crime scene and restart? Enter: 'y' or 'n'.")
            if restart.lower() in ["yes", "y"]:
                #if the user's input to restart is "yes" or "y", the scene_5() function is called
                scene_5()
            elif restart.lower() in ["no", "n"]:
                #if the user's input to restart is "no" or "n", the following will be print and the game will end (using sys.exit())
                print("Goodbye.")
                sys.exit()
        elif murderer_1.lower() == "harry":
            #the following prints
            print("You haven't even met Harry...She was mentioned briefly...What are you doing? You've failed.")
            x()
            restart = input("Would you like to go back to the crime scene and restart? Enter: 'y' or 'n'.")
            #this variable will take the user's input to the above question
            while restart.lower() not in ["yes", "y", "no", "n"]:
                #this while loop will continue to ask the user for a valid input to restart if their input is not in the above list
                restart = input("Would you like to go back to the crime scene and restart? Enter: 'y' or 'n'.")
            if restart.lower() in ["yes", "y"]:
                #if the user's input to restart is "yes" or "y", the scene_5() function is called
                scene_5()
            elif restart.lower() in ["no", "n"]:
                #if the user's input to restart is "no" or "n", the following will be print and the game will end (using sys.exit())
                print("Goodbye.")
                sys.exit()
        elif murderer_1.lower() == "anderson" or murderer_1.lower() == "sally":
            #the following prints
            print("We get it. You hate them. But no way are they smart enough to have committed a murder.")
            x()
            restart = input("Would you like to go back to the crime scene and restart? Enter: 'y' or 'n'.")
            #this variable will take the user's input to the above question
            while restart.lower() not in ["yes", "y", "no", "n"]:
                #this while loop will continue to ask the user for a valid input to restart if their input is not in the above list
                restart = input("Would you like to go back to the crime scene and restart? Enter: 'y' or 'n'.")
            if restart.lower() in ["yes", "y"]:
                #if the user's input to restart is "yes" or "y", the scene_5() function is called
                scene_5()
            elif restart.lower() in ["no", "n"]:
                #if the user's input to restart is "no" or "n", the following will be print and the game will end (using sys.exit())
                print("Goodbye.")
                sys.exit()
    elif murderer.lower() in ["no", "n"]:
        #if the user's input to murderer is "no" or "n", the function x() is called
        x()

class quote:
    """Class defining famous/funny quotes from the episode"""
    def __init__(self, quote, person):
        """Constructor for quote class"""
        self.quote = quote
        self.person = person
    def introduce(self):
        #this method introduces/describes the quote to the player
        print(f"You have discovered the following quote: {self.quote} ~{self.person}")

class clue:
    """Class defining a clue"""
    def __init__(self, name, place):
        """Constructor for clue class"""
        self.name = name
        self.place = place

    def introduce(self):
        #this method introduces/describes the clue to the player
        print(f"You have discovered a new clue: {self.name}. This clue was discovered at {self.place}")

play = input("Would you like to play 'Sherlock: A Study in Pink'? Enter: 'y' or 'n'.")
#this take the user input and asks the player if they want to play the game
if play.lower() == "yes" or play.lower() == "y":
#if the player inputs "yes" or "y", the game will start and the following will print
    print(f"""INTRUCTIONS: Welcome to the game. In this game, you play as the infamous detective Sherlock Holmes. This game is based on the episode of BBC Sherlock, 'A Study in Pink,' and uses dialogue from the show. Your friendship with Lestrade determines how the game progresses. Whenever you see the '<' symbol:
        -press enter to continue
        -type 'clues' to view your current list of clues.
        -type 'quotes' to view the quotes you have unlocked""")

    def different_lestrade():
        """This function continues Scene 1 of the story"""
        #the following prints and the function x() is called
        print("LESTRADE: You know how they never leave notes?")
        x()
        print("YOU: Yeah.")
        x()
        print("LESTRADE: This one did. Will you come?")
        x()
        #the first clue is created based on the clue class. the clue description is listed first in the parentheses followed by the location the clue was found
        clue_1 = clue("Fourth Suicide Note", "Lauriston Gardens")
        #this is a method from the clue class that introduces/describes the first clue found to the player
        clue_1.introduce()
        #this clue is added to the clues list. now when the player wants to look at their list of clues, this clue will be in the list
        clues.append("The Fourth Suicide left a note, while the others did not.")
        #the following prints and the function x() is called to continue the story
        x()
        print("You think for a moment. The only things keeping you from jumping at this opportunity were the few people who worked at the police department that disliked you. It would be difficult to work if they were there as well...")
        x()
        print("YOU: Who's on Forensics?")
        x()
        print("LESTRADE: Anderson.")
        x()
        print("Anderson was one of the few people you knew would not work with you.")
        x()
        print("YOU: Anderson won't work with me.")
        x()
        print("LESTRADE: He won't be your assistant.")
        x()
        print("YOU: But I need an assistant.")
        x()
        print("LESTRADE(almost begging): Will you come?")
        x()
        go_to_lg = input("Lestrade has asked you to go to Lauriston Gardens. How will you respond: 'now' or 'later'?")
        #the above takes the user's input to the previous question
        while go_to_lg.lower() not in ['now', 'later']:
            #this while loop will continue to prompt the user with the go_to_lg variable until they give a valid input from the above list
            go_to_lg = input("Lestrade has asked you to go to Lauriston Gardens. How will you respond: 'now' or 'later'?")
        if go_to_lg.lower() == "now":
            #if the user's input to go_to_lg is "now", the user's friendship with Lestrade increases; the word global is used to show that the varibale being identified was defined outside of the function
            global friendship_lestrade
            friendship_lestrade += 1
            #the following prints and the function x() is called to continue the story
            print(f"Because of your compliance, your friendship level with Lestrade has increased. Your friendship level is now {friendship_lestrade}.")
            x()
            print("YOU: Not in a police car. I'll be right behind you.")
            x()
            print("LESTRADE: Thank you!")
            x()
            print("Lestrade disappeared out the door of your flat, down the stairs and back to his police car, heading to Lauriston Gardens.")
            x()
            print("You couldn't help the smile that appeared on your face. You finally had a case to work on!")
            x()
            print("YOU: Brilliant! And I thought it was going to be a boring evening. Serial suicides, and now a note. Mrs. Hudson, I'll be late -- might need some food.")
            x()
            print("MRS. HUDSON: I'm your landlady, dear, not your housekeeper.")
            x()
            print("YOU: Something cold is fine. John, make yourself at home -- have a cuppa! Don't wait up!")
            x()
        elif go_to_lg.lower() == "later":
            #if the user's input to go_to_lg is "later", the user's friendship with lestrade is decreased
            friendship_lestrade -= 1
            #the following prints and the function x() is called to continue the story
            print(f"Because of your rudeness, your friendship level with Lestrade has decreased. Your friendship level is now {friendship_lestrade}.")
            x()
            print("YOU (trying to hide your excitement): I'll get there when I get there.")
            x()
            print("LESTRADE: Fine. Just get there sooner rather than later.")
            x()
            print("Lestrade disappeared out the door of your flat, down the stairs and back to his police car, heading to Lauriston Gardens.")
            x()
            print("You couldn't help the smile that appeared on your face. You finally had a case to work on!")
            x()
            print("YOU: Brilliant! And I thought it was going to be a boring evening. Serial suicides, and now a note. Mrs. Hudson, I'll be late -- might need some food.")
            x()
            print("MRS. HUDSON: I'm your landlady, dear, not your housekeeper.")
            x()
            print("YOU: Something cold is fine. John, make yourself at home -- have a cuppa! Don't wait up!")
            x()

    def scene_1():
        """"Scene one of the game begins when this function is called"""
        #the story begins. lines of text are printed one by one for the player to read followed by calling the x() function to start the story
        print("Introduction:")
        print("Your name is Sherlock Holmes, an infamous detective who lives in present-day London. You have recently moved into a flat at 221B Baker street with Dr. John Watson. Upon meeting Watson, you discovered that he was an army doctor. Currently, you are sitting in your flat when Mrs. Hudson, your landlady, asks you your opinion about the recent suicides that have been reported in the paper. For some reason, you had a feeling that the suicides weren't actually. This is where the case begins.")
        x()
        possible_murderers.append("mrs. hudson")
        print("MRS. HUDSON: What about these suicides, then, Sherlock? Thought that would be right up your street. Three of them, exactly the same. That's a bit funny, isn't it?")
        x()
        print("You suddenly get a feeling. You glance out the window and see a blue flashing light coming from a police car parked below your flat.")
        x()
        print("YOU: Four. There's been a fourth. And there's something different this time.")
        x()
        print("MRS. HUDSON: A fourth? How do you know?")
        x()
        print("You hear feet thumping on the stairs. In bursts Lestrade, a detective from the local police force. Lestrade often uses you as a consultant when the police are out of options.")
        x()
        print("YOU: Where?")
        x()
        print("LESTRADE: Brixton. Lauriston Gardens.")
        possible_murderers.append("lestrade")
        x()
        print("Lestrade wouldn't be here unless something was different this time.")
        x()
        different = input("What do you want to say to Lestrade? Enter: 'sassy remark' or 'question'.")
        #the above variable takes the user's input on the how they want to respond to Lestrade
        while different.lower() not in ['sassy remark', 'question']:
            #this while loop will continue to ask the user for a valid input to different if their input is not in the above list
            different = input("What do you want to say to Lestrade? Enter: 'sassy remark' or 'question'.")
        if different.lower() == "sassy remark":
            #if the user's input to different is "sassy remark", the user's friendship with lestrade will decrease; the world global is used to show that the variable being identified was defined outside of the function
            global friendship_lestrade
            friendship_lestrade -= 1
            #the following will print
            print(f"Your friendship with Lestrade has decreased because of your sassy remark. Your friendship level is now {friendship_lestrade}.")
            x()
            print("YOU: You wouldn't have come to get me if there wasn't anything new and the police couldn't figure it out.")
            x()
            #the function different_lestrade() is called and will continue the story
            different_lestrade()
        elif different.lower() == "question":
            #if the user's input to different is "question", the user's friendship with Lestrade will increase
            friendship_lestrade += 1
            #the following will print
            print(f"Your friendship level with Lestrade has increased because of your genuine question. Your friendship level is now {friendship_lestrade}.")
            x()
            print("What's different about this one?")
            x()
            #the function different_lestrade() called and will continue the story
            different_lestrade()

    #this calls the previously defined scene_1() function
    scene_1()

    def assistant_john():
        """This function continues the story when the player picks John as their assistant to take to the crime scene in Scene 2."""
        #the story is continued by printing lines of text followed by the previously defined function x()
        print("YOU (to John): You're a doctor.")
        x()
        print("John looks up startled.")
        x()
        print("YOU: In fact, you're an army doctor.")
        x()
        print("JOHN: Yes.")
        x()
        print("YOU: Seen a lot of injuries then?")
        x()
        print("JOHN: Well, yes.")
        x()
        print("YOU: Bit of trouble too, I bet.")
        x()
        print("JOHN: Of course, yes. Enough for a lifetime. Far too much.")
        x()
        print("YOU: Want to see some more?")
        x()
        print("JOHN: Oh, God, yes!")
        x()
        print("YOU: Get your coat.")
        x()
        print("You both rush for the door, but Mrs. Hudson stops you on your way out.")
        x()
        print("JOHN: Sorry, Mrs. Hudson, I’ll skip the cuppa -- off out.")
        x()
        print("MRS. HUDSON: Both of you?")
        x()
        print("YOU: Impossible suicides - four of them. No point in sitting at home when there’s finally something fun going on!")
        x()
        print("MRS. HUDSON: Look at you, all happy. It's not decent.")
        x()
        print("YOU: Who cares about decent? The game, Mrs. Hudson, is on!")
        x()
        #the first quote is created based on the quote class. the quote itself is listed first in the parentheses followed by the person who said the quote
        quote_1 = quote("The game, Mrs. Hudson, is on!", "Sherlock Holmes")
        #this is a method from the quote class that introduces/describes the first quote found to the player
        quote_1.introduce()
        #this quote is added to the list of quotes
        quotes.append("The game, Mrs. Hudson, is on! ~Sherlock Holmes")
        x()
        print("You and John run out of the flat. You hail a cab and climb inside, telling the cabbie to head to Lauriston Gardens.")

    def scene_2():
        """Scene 2 will begin when this function is called"""
        assistant_decision = input("You put on your black trench coat and blue scarf and dash out the door. You stop outside the door after exiting the flat. You should get going, but you need an assistant. Who should you ask to be you assistant, Mrs. Hudson or John Watson? Enter 'john watson' or 'mrs. hudson'.")
        #this takes the user input of who they want to take to the crime scene with them
        possible_assistants = ["john watson", "mrs. hudson"]
        #this is the list of acceptable inputs when the player is prompted with the previously defined assistant_decision
        while assistant_decision.lower() not in possible_assistants:
            #this is a while loop that continues to ask for the player's input until their input for assistant_decision is in possible_assistants
            assistant_decision = input("You put on your black trench coat and blue scarf and dash out the door. You stop outside the door after exiting the flat. You should get going, but you need an assistant. Who should you ask to be you assistant, Mrs. Hudson or John Watson? Enter 'john watson' or 'mrs. hudson'.")
        if assistant_decision.lower() == "mrs. hudson":
            #the following will print if the user's input to assistant_decision is 'mrs. hudson'
            print("Mrs. Hudson probably wouldn't do well at a crime scene.")
            take_hudson = input("Are you sure you want to bring Mrs. Hudson? Enter: 'y' or 'n'.")
            #this asks for the user's input on if they are sure they want to take Mrs. Hudson to the crime scene
            while take_hudson.lower() not in ["yes", "y", "no", "n"]:
                #this while loop continues to ask for the user's input to take_hudson while it is not in the above list
                take_hudson = input("Are you sure you want to bring Mrs. Hudson? Enter: 'y' or 'n'.")
            if take_hudson.lower() == "y" or take_hudson.lower() == "yes":
                #if the user's input for take_hudson is 'yes' or 'y', the following will be printed
                print("You take Mrs. Hudson to the crime scene. She wasn't that helpful. The case was never solved. You have failed.")
                restart = input("Would you like to go back to the last scene and restart? y or n?")
                #this takes the user input on whether or not they want to restart the game after they have failed by bringing Mrs. Hudson to the crime scene
                if restart.lower() == "y" or restart.lower() == "yes":
                    #if the user's input to restart is 'yes' or 'y', scene_2() is called and the game will continue
                    scene_2()
                elif restart.lower() == "n" or restart.lower() == "no":
                    #if the user's input to restart is "no" or "n", the following will print and the game will end (using sys.exit())
                    print("Goodbye.")
                    sys.exit()
            elif take_hudson.lower() == "no" or take_hudson.lower() == "n":
                #if the user's input to take_hudson is "n" or "no", the following will be printed and the assistant_john() function will be called
                print("You should ask John.")
                assistant_john()
        elif assistant_decision.lower() == "john watson":
            #if the user's input to assistant_decision is "john watson", the following will print and the assistant_john() function will be called
            print("Good choice. You head back inside to speak to John.")
            x()
            assistant_john()

    #the previously defined scene_2() function will be called
    scene_2()

    def job_question_response():
        """This function continues the conversation between the user and John while they are on their way to Lauriston Gardens"""
        print("YOU: I'm a consulting detective. Only one in the world. I invented the job.")
        x()
        #the second quote is created based off of the quote class
        quote_2 = quote("I'm a consulting detective. Only one in the world. I invented the job.", "Sherlock Holmes")
        #the second quote is introduced to the user based on the introduce method of the quote class
        quote_2.introduce()
        #this quote is added to the quotes list
        quotes.append("I'm a consulting detective. Only one in the world. I invented the job. ~Sherlock Holmes")
        x()
        #the following prints and the x() function is called to continue the story
        print("JOHN: What does that mean?")
        x()
        print("YOU: It means that when the police are out of their depth - which is always - they consult me.")
        x()
        print("JOHN: Ah...")
        x()
        print("Silence fills the car.")
        x()
        print("When you first met John, the first thing you did was analyze him like you do with all people. You then asked him  'Afghanistan or Iraq?' because you had come to the conclusion that he was an army doctor, but could not come to the conclusion as to where he was an army doctor. He seemed surprised by this question. You decide to bring this up to break the silence.")
        x()
        print("YOU: When I first met you, I asked Afghanistan or Iraq. You seemed surprised.")
        x()
        print("JOHN: How did you know?")
        tell_question = input("How would you like to answer? Enter 'tell' OR 'later'.")
        #the above variable take the user's input on whether or not they want to tell John how they knew
        possible_tell_question = ['tell', 'later']
        #the above list is the list of acceptable inputs for the tell_question variable
        while tell_question.lower() not in possible_tell_question:
            #this while loop will continue to ask the user the tell_question if their input is not in the possible_tell_question list
            tell_question = input("How would you like to answer? Enter 'tell' OR 'later'.")
        if tell_question.lower() == "tell":
            #if the user's input to tell_question is "tell", the following will print
            print("YOU: I didn't know. I saw.")
            x()
            print("You then begin to explain all of the information you found out about John when you analyzed him that led you to your question.")
            x()
            print("YOU: Tanned face, but no tan above the wrists. You've been abroad but not sunbathing.")
            x()
            print("YOU: Your haircut and the way you hold yourself says military - but your conversation as you entered the room says you trained at Barts. So army doctor. Obvious!")
            x()
            print("YOU: Your limp is really bad when you walk, but you don’t ask for a chair when you stand, like you’ve forgotten about it - so it’s at least partly psychosomatic. That says the circumstances of the original injury were traumatising - wounded in action then.")
            x()
            print("YOU: Wounded in action, a suntan. Afghanistan or Iraq?")
            x()
            print("You were being a show off.")
            x()
            show_off = input("Do you want to continue analyzing John? Enter: 'y' or 'n'.")
            #the above variable takes the user's input on whether or not they want to continue analyzing John
            possible_show_off = ["yes", "y", "no", "n"]
            #the above list are the acceptable inputs for the show_off variable
            while show_off.lower() not in possible_show_off:
                #this while loop will continue to prompt the user with the show_off variable until they provide an input that is in possible_show_off
                show_off = input("Do you want to continue analyzing John? Enter: 'y' or 'n'.")
            if show_off.lower() == "y" or show_off.lower() == "yes":
                #if the user's input to show_off is "y" or "yes", the following will print
                print("YOU: Then there’s your brother --")
                x()
                print("You grab John's phone out of his hand and examine it.")
                x()
                print("YOU: Your phone. Expensive, email enabled, mp3 player - you’re looking for a flatshare, you wouldn’t waste money on this. It’s a gift then.")
                x()
                print("YOU: Scratches - not just one, but many over time. Been in the same pocket as keys and coins. The man in front of me wouldn’t treat his one luxury item like this, so there’s been a previous owner. Next bit’s easy - you know it already.")
                x()
                print("JOHN: The engraving.")
                x()
                possible_murderers.append("harry")
                print("The engraving reads 'To Harry From Clara xxx'")
                x()
                print("YOU: Harry Watson - clearly a family member who’s given you his old phone. Not your father - this is a young man’s gadget. Could be a cousin, but you’re a war hero who can’t find a place to live - unlikely you’ve got an extended family, certainly not one you’re close to. So - brother it is.")
                x()
                print("YOU: Now Clara, who’s Clara - three kisses says it’s a romantic attachment, the expense of the phone says wife not girlfriend.")
                x()
                print("YOU: She must have given it to him recently, this model’s only six months old. It’s a marriage in trouble then - six months on he’s just given it away. If she’d left him, he’d probably have kept the phone - people do, sentiment - but no, he wanted rid of it: he left her. He gave the phone to you - that says he wants you to stay in touch.")
                x()
                harry_question = input("You have a hunch about Harry. Do you want to mention it to John? Enter: 'y' or 'n'.")
                #the above variable takes the user input on whether or not they want to ask John about Harry
                possible_harry_question = ["yes", "y", "no", "n"]
                #the above list are the acceptable inputs for the harry_question variable
                while harry_question.lower() not in possible_harry_question:
                    #this while loop will continue to ask the user the harry_question variable while their input is not in the possible_harry_question list
                    harry_question = input("You have a hunch about Harry. Do you want to mention it to John? Enter: 'y' or 'n'.")
                if harry_question.lower() == "y" or harry_question.lower() == "yes":
                    #if the user's input to harry_question is "y" or "yes", the following will print
                    print("YOU: You’re looking for cheap accommodation, but you’re not going to your brother for help - that says you’ve got problems with him. Maybe you liked his wife, maybe you don’t like his drinking --")
                    x()
                    print("JOHN: How can you possibly know about the drinking?")
                    x()
                    print("YOU: Shot in the dark -- good one though. The power connection.")
                    x()
                    print("YOU: Tiny little scuff marks all round it - he plugs it in every night to recharge, but his hands are shaking. Never see those marks on a sober man’s phone, never see a drunk’s without them.")
                    x()
                    print("JOHN: That was...amazing.")
                    x()
                    print("YOU: Do you think so?")
                    x()
                    print("JOHN: Well, of course it was. It was extraordinary. Quite extraordinary.")
                    x()
                    print("You were quite proud of yourself for impressing John.")
                    x()
                    print("YOU: That's not what people usually say.")
                    x()
                    print("JOHN: What do people usually say?")
                    x()
                    print("YOU: Piss off.")
                    x()
                    print("Curiosity was getting the best of you. You were wondering if you had gotten everything right about John.")
                    x()
                    correct_question = input("Do you want to ask John if you got everything correct? Enter: 'y' or 'n'.")
                    #this variable takes the user's input on whether or not they want to ask John if they got everything correct about him
                    possible_correct_question = ["yes", "no", "y", "n"]
                    #the above list is all of the acceptable inputs for the variable correct_question
                    while correct_question.lower() not in possible_correct_question:
                        #this while loop will continue to ask the user the correct_question variable while their input is not in the possible_correct_question list
                        correct_question = input("Do you want to ask John if you got everything correct? Enter: 'y' or 'n'.")
                    if correct_question.lower() == "y" or correct_question.lower() == "yes":
                        #if the user's input to correct_question is "y" or "yes", the following will print
                        print("YOU: Did I get anything wrong?")
                        x()
                        print("JOHN: Harry and me don’t get on, never have. Clara and Harry split up three months ago, they’re getting a divorce. Harry’s a drinker --")
                        x()
                        print("YOU: Spot on, then! Didn’t expect to be right about everything.")
                        x()
                        print("JOHN: --Harry is short for Harriet.")
                        x()
                        print("YOU: Harry is your sister.")
                        x()
                        print("JOHN: Look, exactly what am I supposed to be doing here?")
                        x()
                        print("YOU: Your sister.")
                        x()
                        print("JOHN: No, seriously, why am I here?")
                        x()
                        print("YOU: There's always something!")
                        x()
                        print("YOU: We are here.")
                        x()
                    elif correct_question.lower() == "no" or correct_question.lower() == "n":
                        #if the user's input to correct_question is "n" or "no", the following prints
                        print("YOU: We are here.")
                        x()
                else:
                    #if the user's input to harry_question is not "y" or "yes", the following prints
                    print("YOU: We are here.")
                    x()
            elif show_off.lower() == "n" or show_off.lower() == "no":
                #if the user's input to show_off is "n" or "no", the following prints
                print("YOU: We are here.")
                x()
        elif tell_question.lower() == "later":
            #if the user's input to tell_question is "later", the following prints
            print("YOU: We are here.")
            x()

    def scene_3():
        """"Scene three of the game begins when this function is called"""
        #the following prints and x() is called to continue the story
        x()
        print("You and John are riding in the cab on your way to Lauriston Gardens, and you notice John keeps glancing at you.")
        x()
        print("YOU: Okay, you've got questions.")
        x()
        print("JOHN: Where are we going?")
        x()
        print("YOU: Crime scene, next.")
        x()
        print("JOHN: Who are you? What do you do?")
        x()
        job_question = input("How would you like to answer? Enter: 'consulting detective' OR 'sassy remark'.")
        #this variable take the user's input on how they want to respond to John's question about their job
        possible_job_question = ["consulting detective", "sassy remark"]
        #the above list are the acceptable inputs for the job_question variable
        while job_question.lower() not in possible_job_question:
            #this loop will continue to ask the user the job_question while their input is not in possible_job_question list
            job_question = input("How would you like to answer? Enter: 'consulting detective' OR 'sassy remark'.")
        if job_question.lower() == "consulting detective":
            #if the user's input to job_question is "consulting detective", the job_question_response() function is called
            job_question_response()
        elif job_question.lower() == "sassy remark":
            #the following prints and x() is called to continue the story
            print("YOU: What do you think?")
            x()
            print("JOHN: I'd say you were a private detective, but --")
            x()
            print("YOU: But?")
            x()
            print("JOHN: The police doesn't go to priavte detectives.")
            x()
            #the job_question_response() function is called
            job_question_response()

    #the previously defined function scene_3() is called
    scene_3()

    def scene_4():
        """Scene four of the game begins when this function is called"""
        #the following prints and x() is called to continue the story
        print("You and John have arrived at Lauriston Gardens. You both exited the cab and walked up to the police tape surrounding the building.")
        x()
        print("SALLY: Hello, freak.")
        x()
        possible_murderers.append("sally")
        #the element "sally" is added to the possible_murderers list
        #the following prints
        print("Sally works at the police department. She is also a person you dislike.")
        x()
        print("YOU: I'm here to see Detective Inspector Lestrade.")
        x()
        print("SALLY: Why?")
        x()
        print("YOU: I think he wants me to take a look.")
        x()
        print("SALLY: Well, you know what I think, don't you?")
        x()
        print("YOU: Always, Sally.")
        x()
        print("SALLY (into her walkie talkie): Freak's here. Bringing him in.")
        x()
        #the word global is used to show that the varibale being identified was defined outside of the function
        global friendship_lestrade
        if friendship_lestrade >= 2:
            #if the reader's friendship level with Lestrade is greater than or equal to 2, the following prints and x() is called to continue the story
            print("Your friendship level with Lestrade was high enough for him to let you into the crime scene. Congrats!")
            x()
            print("LESTRADE (through the walkie talkie): Bring them in.")
            x()
            print("Sally guides you and John into the building and brings you upstairs to the second floor. You walk into the room where the crime was committed. Lestrade is there.")
            x()
            print("LESTRADE (talking about the victim): Jennifer Wilson, according to her credit cards - we’re running them now for contact details. Hasn’t been here long - some kids found her.")
            x()
            print("A woman in a bright pink coat, and pink shoes, lies dead, sprawled face down on the floor. The room remained silent, but you couldn't think.")
            x()
            #the second clue is made from the clue class; the clue description is listed first in the parentheses followed by the location where it was found
            clue_2 = clue("Jennifer Wilson's outfit is completely pink", "Lauriston Gardens")
            #the introduce method of the clue class is used to introduce/describe the clue to the user
            clue_2.introduce()
            #the clue is added to the clues list
            clues.append("Jennifer Wilson's outfit is completely pink")
            x()
            #the third clue is made from the clue class; the clue description is listed first in the parentheses followed by the location where it was found
            clue_3 = clue("Jennifer Wilson's outfit shows she is a professional person", "Lauriston Gardens")
            #the introduce method of the clue class is used to introduce/describe the clue to the user
            clue_3.introduce()
            #the clue is added to the clues list
            clues.append("Jennifer Wilson's outfit shows she is a professional person")
            #the following is printed and the x() function is called, so the story can continue
            x()
            print("YOU: Shut up!")
            x()
            print("LESTRADE: Didn't say anything.")
            x()
            print("YOU: You were thinking. It's annoying.")
            x()
            #the third quote is made from the quote class; the quote is listed first in the parentheses followed by the person who said the quote
            quote_3 = quote("You were thinking. It's annoying.", "Sherlock Holmes")
            #the introduce method of the quotes class is used to introduce/describe the quote to the user
            quote_3.introduce()
            #the quote is added to the quotes list
            quotes.append("You were thinking. It's annoying. ~Sherlock Holmes")
            x()
            examining = True
            #the variable examining is set equal to True
            options_examine = ["hand", "coat", "jewelry", "leg"]
            #the above list is the list of possible options for the examine variable
            while examining:
                #this while loop will ask the reader the examine variable while the number of elements in the options_examine list is greater than 0
                examine = input(f"You move closer to the body to examine it. Where do you want to examine? {', '.join(options_examine)} ")
                #the above variable prompts the user to  search for clues at the crime scene
                while examine.lower() not in options_examine:
                    #this while loop will prompt the user with the examine variable while their input isn't in the options_examine list
                    examine = input(f"You move closer to the body to examine it. Where do you want to examine? {', '.join(options_examine)} ")
                if examine.lower() == "hand":
                    #if the user's input is "hand", the following will print
                    print("With her left hand, Wilson had scratched a word into the wooden floorboards. The word is 'Rache.'")
                    x()
                    print("'Rache' means 'revenge' in German.")
                    x()
                    print("What else could that mean?")
                    x()
                    print("You think for a moment...")
                    x()
                    print("Rachel.")
                    x()
                    clue_4 = clue("Jennifer scratched the word 'RACHE' into the floorboards. You believe she didn't finish and was instead writing 'Rachel'", "Lauriston Gardens")
                    #the above clue was made from the clues class; the description of the clue is listed first in the parentheses and the location where the clue was discovered is listed second
                    clue_4.introduce()
                    #the clue is described/introduced to the user by using the introduce method of the clue class
                    clues.append("Jennifer Wilson scratched 'Rachel' into the floorboards")
                    #the clue is then added to the clues list
                    x()
                    print("You look at Wilson's fingernails. All were painted pink to match her coat and heels. The only nails chip were those she used to carve into the wooden floor.")
                    clue_5 = clue("Jennifer Wilson does not work with her hands", "Lauriston Gardens")
                    #the above clue was made from the clues class; the description of the clue is listed first in the parentheses and the location where the clue was discovered is listed second
                    clue_5.introduce()
                    #the clue is described/introduced to the user by using the introduce method of the clue class
                    clues.append("Jennifer Wilson did not work with her hands")
                    #the clue is then added to the clues list
                    x()
                elif examine.lower() == "coat":
                    #the following will print and the x() function will be called to continue the story
                    print("You run your gloved hand over the woman's coat. The coat was wet.")
                    x()
                    print("You pull a fold-away umbrella out of her coat pocket. It was dry.")
                    x()
                    print("You run your hand under the collar of the woman's coat. The collar is wet.")
                    x()
                    clue_6 = clue("Jennifer Wilson was outside in a windy rain storm", "Lauriston Gardens")
                    #the above clue was made from the clue class; the description of the clue is listed first in the parentheses and the location where the clue was discovered is listed second
                    clue_6.introduce()
                    #the clue is described/introduced to the user by using the introduce method of the clue class
                    clues.append("Jennifer Wilson was outside in a rain storm prior to her death.")
                    #the clue is added to the clues list
                    x()
                elif examine.lower() == "jewelry":
                    print("You examine the woman's left hand. The woman was wearing her wedding ring. Unlike all of her other jewelry, her wedding ring was dirty.")
                    x()
                    clue_7 = clue("Jennifer Wilson was unhappily married", "Lauriston Gardens")
                    #the above clue was made from the clue class; the description of the clue is listed first in the parentheses and the location where the clue was discovered is listed second
                    clue_7.introduce()
                    #the clue is described/introduced to the user by using the introduce method of the clue class
                    clues.append("Jennifer Wilson was unhappily married.")
                    #the clue is added to the clue list
                    x()
                    print("You take off Wilson's wedding ring. While the outside is dirty, the inside is clean like her other jewelry, meaning the ring is regularly removed. You believe that Wilson was probably an adulter whose lovers did not know she was married.")
                    x()
                    clue_8 = clue ("Jennifer Wilson was an adulterer", "Lauriston Gardens")
                    #the above clue was made from the clue class; the description of the clue is listed first in the parentheses and the location where the clue was discovered is listed second
                    clue_8.introduce()
                    #the clue is described/introduced to the user by using the introduce method of the clue class
                    clues.append("Jennifer Wilson was an adulterer.")
                    #the clue is added to the clue list
                    x()
                elif examine.lower() == "leg":
                    #the following is printed and the x() function is called to continue the story
                    print("You look at the back of Wilson's right leg. It is covered in small splashes, probably from a suitcase she was carrying.")
                    x()
                    clue_9 = clue("Wilson had a suitcase with her", "Lauriston Gardens")
                    #the above clue was made from the clue class; the description of the clue is listed first in the parentheses and the location where the clue was discovered is listed second
                    clue_9.introduce()
                    #the clus is introduced/described to the user by using the introduce method of the clue class
                    clues.append("Wilson had a suitcase with her.")
                    #the clue is added to the clue list
                    x()
                options_examine.remove(examine)
                #the above removes the user's input from the options_examine list
                if len(options_examine) == 0:
                    #if the length of the options_examine list is 0, examining is False and the while loop will end
                    examining = False
            possible_murderers.append("husband")
            possible_murderers.append("lover")
            #"lover" and "husband" are added to the possible_murderers list
        elif friendship_lestrade < 2:
            #if your friendship with Lestrade is less, than 2, the following will print and the game will end (using sys.exit())
            print("Your friendship level with Lestrade was too low. He was upset with you and did not let you into the crime scene. You lose!")
            sys.exit()

    #the previously defined scene_4() is called
    scene_4()

    def tell_lestrade():
        """This function continues scene 5 when called"""
        #the following prints and the x() function is called to continue the story
        print("You have come up with many conclusions about Jennifer Wilson:")
        x()
        print("YOU: Victim is in her late forties. Professional person going by her clothes - I’d guess something in the media, going by the frankly alarming shade of pink. She’s travelled from Cardiff today, intending to stay for one night - that’s obvious from the size of her suitcase -- ")
        x()
        print("LESTRADE: Suitcase?")
        x()
        print("YOU: Suitcase, yes. She’s been married for at least ten years, but not happily. She’s had a string of lovers, but none of them have known she was married --")
        x()
        print("LESTRADE: For God's sake. If you're just making this up...")
        x()
        print("YOU: The wedding ring. The rest of her jewelery has been regularly cleaned, but not her wedding rings - state of her marriage, right there. The inside of the rings are shinier than the outside - that means they’re regularly removed; the only polishing they get is when she works them off her finger. It’s not for work - look at her nails, she doesn’t work with her hands - so what, or rather who, does she remove her rings for? Clearly not one lover - she’d never sustain the fiction of being single over time - so more likely a string of them. Simple!")
        x()
        print("JOHN: Brilliant! Sorry...")
        x()
        print("LESTRADE: Cardiff?")
        x()
        print("YOU: Obvious, isn't it?")
        x()
        print("JOHN: Not obvious to me.")
        x()
        print("YOU: Dear God, what's it like in your funny little brains? It must be so boring. Her coat!")
        x()
        #the fourth quote is made based off of the quote class
        quote_4 = quote("Dear God, what's it like in your funny little brains? It must be so boring.", "Sherlock Holmes")
        #the fourth quote is introduced to the user based on the introduce method of the quotes class
        quote_4.introduce()
        #the quote is added to the quotes list
        quotes.append("Dear God, what's it like in your funny little brains? It must be so boring. ~Sherlock Holmes")
        #the following prints and x() is called to continue the story
        x()
        print("YOU: Her coat. It’s slightly damp - she’s been in heavy rain within the last few hours. No rain anywhere in London in that time. Under her coat collar is damp too. She turned it up against the wind! She’s got an umbrella in her left pocket but it’s unused and dry. Not just wind, strong wind - too strong to use her umbrella. We know from her suitcase that she’s staying over night so she must have a come a decent distance. But she can’t have travelled more than two or three hours, cos her coat hasn’t dried. So where has there been heavy rain and strong wind within the radius of that travel time? I did a quick search on my phone, and the answer is Cardiff.")
        x()
        print("JOHN: Fantastic!")
        x()
        print("You and Lestrade look at John.")
        x()
        print("SHERLOCK: Do you know you do that out loud?")
        x()
        print("JOHN: ... sorry, I'll shut up.")
        x()
        print("YOU: No, it’s fine.")
        x()
        print("LESTRADE: Why do you keep saying suitcase?")
        x()
        print("YOU: Yeah, where is it? She must have a phone or an organiser - we can find out who Rachel is.")
        x()
        print("LESTRADE: She was writing Rachel?")
        x()
        print("YOU: No, she was leaving an angry note in German - of course she was writing Rachel. No other word it can be. Question is, why did she wait till she was dying to write it?")
        x()
        print("LESTRADE: How do you know she had a case?")
        x()
        print("YOU: Back of her right leg. Tiny splashes on the heel and calf, not present on the left. She was dragging a wheeled suitcase behind her, with her right hand - you don’t get that splash pattern any other way. Smallish case, going by the spread. Case that size, woman this clothes-conscious - could only be an overnight bag. So we know she was staying one night. Now where is it - what have you done with it?")
        x()
        print("You bend over the body to see if you missed anything.")
        x()
        print("LESTRADE: There wasn’t a case.")
        x()
        print("There should be a case...")
        x()
        print("YOU: ... say that again.")
        x()
        print("LESTRADE: There wasn’t a case. There was never any suitcase here.")
        x()
        print("You are completely and utterly confused. There HAS to be a suitcase.")
        x()
        print("You stand up, shove past Lestrade and stride onto the landing of the stairs.")
        x()
        print("YOU (yelling to everybody in the building): Suitcase! Did anyone find a suitcase - was there a suitcase in this house.")
        x()
        print("Lestrade emerges from the room behind you.")
        x()
        print("LESTRADE: Sherlock, there was no case.")
        x()
        print("You mind is swimming, trying to understand where the suitcase is.")
        x()
        print("YOU: But they take the poison themselves. They chew and swallow the pills themselves, there are clear signs - even you lot couldn’t miss them.")
        x()
        print("LESTRADE: Right, yes, thanks - and?")
        x()
        print("YOU: ... it’s murder. All of them. I don’t know how, but they’re not suicides, they’re killings - serial killings. We’ve got a serial killer. Love those, there’s always something to look forward to.")
        x()
        print("LESTRADE: Why? Why are you saying that?")
        x()
        print("YOU: Where’s her case? Come on, where is it? Did she eat it? Someone else was here - and they took the case. So the killer must have driven her here - forgot the case was in the car ...")
        x()
        print("JOHN: Maybe she checked into her hotel, left her case there.")
        x()
        print("YOU: She never made it to her hotel. She colour coordinates her lipstick and her shoes. She always looks immaculate. Look at her hair, she’d never have left a hotel with her hair still like --")
        x()
        print("And you have a sudden realization. Pink coat... Pink nails... Pink shoes... Pink suitcase.")
        x()
        print("YOU: Oh. Oh!")
        x()
        print("JOHN: ...Sherlock?")
        x()
        print("You bound down the stairs.")
        x()
        print("LESTRADE: What? What is it?")
        x()
        print("YOU: Serial killers, always hard. You’ve got to wait for them to make a mistake ...")
        x()
        print("LESTRADE: We can’t just wait!")
        x()
        print("YOU: Oh, we’re done waiting. Look at her! Really, look! Houston, we have a mistake! Get on to Cardiff, find Jennifer Wilson’s family and friends - find Rachel.")
        x()
        print("LESTRADE: Of course, yes. But what mistake??")
        x()
        print("YOU (yelling up from the bottom of the stairs): Pink!!")
        x()

    def scene_5():
        """"Scene 5 of the game begins when this function is called"""
        #the function murderer() is called
        murderer()
        #the following prints and the x() is called to continue the story
        print("LESTRADE: Got anything?")
        x()
        print("YOU: Not much.")
        x()
        print("Anderson walks in. He works with the police department.")
        x()
        #"anderson" is added to the possible_murderers list
        possible_murderers.append("anderson")
        #the following prints and the x() is called to continue the story
        print("ANDERSON: She's German. Rache is German for revenge. She could be trying to tell us something.")
        x()
        print("YOU: Yes, thank you for your input.")
        x()
        print("LESTRADE: She's German?")
        x()
        print("YOU: Of course she's not German. She's from out of town though. Planned to spend a single night in London, before returning home to Cardiff. So far, so obvious.")
        x()
        print("JOHN: Sorry, obvious?")
        x()
        print("LESTRADE: What about the message though?")
        x()
        message = input("Do you want to ignore Lestrade or tell him what you have discovered? Enter: 'ignore' or 'discuss'.")
        #the above variable take the user's input
        while message.lower() not in ["ignore", "discuss"]:
            #this while loop will ask the user the message variable while the user's input is not in the above list
            message = input("Do you want to ignore Lestrade or tell him what you have discovered? Enter: 'ignore' or 'discuss'.")
        if message.lower() == "ignore":
            #if the input to message is "ignore", the user's friendship with lestrade decreased by 1 and the following prints and x() is called to continue the story
            global friendship_lestrade
            friendship_lestrade -= 1
            print(f"Your rudeness towards Lestrade was offputting. Your friendship level with Lestrade has decreased and is now {friendship_lestrade}.")
            x()
            print("YOU: Dr. Watson, what do you think?")
            x()
            print("JOHN: Of the message?")
            x()
            print("YOU: Of the body. You're a medical man.")
            x()
            print("LESTRADE: We have a whole team right outside --")
            x()
            print("YOU: They won't work with me.")
            x()
            print("LESTRADE: Sherlock, I'm breaking every rule letting you in here.")
            x()
            print("YOU: Yeah, 'cause you need me.")
            x()
            print("LESTRADE: Yes, I do. God, help me.")
            x()
            print("You walk over to the body and look back at John, who is just standing near the door.")
            x()
            print("YOU: Dr. Watson!")
            x()
            print("John nervously looks at Lestrade.")
            x()
            print("LESTRADE: Oh, do as he says, help yourself.")
            x()
            print("John walks over and you both kneel over the body.")
            x()
            print("YOU: Well?")
            x()
            print("JOHN (whispering): What am I doing here?")
            x()
            print("YOU (whispering): Helping me make a point")
            x()
            print("JOHN: I'm supposed to be helping you pay the rent!")
            x()
            print("YOU: Yeah, this is more fun.")
            x()
            print("JOHN: Fun?! There is a woman lying dead!")
            x()
            print("You ignore John's outburst.")
            x()
            print("YOU: Perfectly sound analysis, but I was hoping you'd go deeper.")
            x()
            print("John bends over the woman and begins examining her.")
            x()
            print("JOHN: Asphyxiation probably. Passed out, and choked on her own vomit. Can’t smell any alcohol on her - could’ve been a seizure, possibly drugs.")
            x()
            print("YOU: You know it was. You've read the papers.")
            x()
            print("JOHN: She's one of the suicides. The fourth.")
            x()
            print("LESTRADE: Sherlock, I need anything you've got.")
            x()
            #the function tell_lestrade() is called
            tell_lestrade()
        elif message.lower() == "discuss":
            #if the user's input to message is "discuss" the following happens
            if friendship_lestrade == 5:
                #if the the user's friendship level with Lestrade is 5, the following prints and the tell_lestrade() function is called
                print(f"Because of your compliance, your friendship level with Lestrade remained the same and is still {friendship_lestrade}.")
                x()
                tell_lestrade()
            elif friendship_lestrade < 5:
                #if the user's friendship level with Lestrade is less than 5, the user's friendship with Lestrade increases by 1 and tell_lestrade() is called
                friendship_lestrade += 1
                print(f"Because of your compliance, your friendship level with Lestrade has increased. You current friendship level with Lestrade is {friendship_lestrade}.")
                x()
                tell_lestrade()

    scene_5()

    def found_suitcase():
        """This function continues scene 6 when called"""
        #the following prints and the x() function is called to continue the story
        print("You look over to John and see him looking down at the suitcase on the coffee table. John looks puzzled.")
        x()
        print("JOHN: That’s ... that’s the pink lady’s case ... Jennifer Wilson’s case...")
        x()
        print("YOU: Yes, of course it is. Oh, I should probably mention that I didn’t kill her.")
        x()
        print("JOHN: ... I never said you did.")
        x()
        print("YOU: Why not? Given the text I just sent, and the fact I have this case, it would be a perfectly logical assumption.")
        x()
        print("JOHN: Do people usually assume you’re the murderer?")
        x()
        print("YOU: Now and then, yes.")
        x()
        print("JOHN: ... Okay. So how did you get this?")
        x()
        print("YOU: By looking.")
        x()
        print("JOHN: Where?")
        x()
        print("YOU: The killer must have driven her to Lauriston Gardens. He could only keep her case by accident, if it was in a car. No one could be seen with this case without attracting attention - particularly a man, which is statistically likely. So obviously he’d feel compelled to get rid of it the moment he noticed he still had it - wouldn’t have taken him more than five minutes to realise his mistake.")
        x()
        print("YOU: I checked every back street wide enough for a car within five minutes of Lauriston Gardens and looked for anywhere you could dispose of a bulky object without being observed. Took me less than an hour to find the right skip.")
        x()
        print("JOHN: Pink. You got all that 'cause you realized the case would be pink.")
        x()
        print("YOU: It had to be pink. Obviously.")
        x()
        print("JOHN: Why didn't I think of that?")
        x()
        print("YOU: Because you're an idiot.")
        x()
        print("John looks hurt by your words.")
        x()
        print("YOU: Don’t look like that - practically everyone is. (pointing at the case) Now look - do you see what’s missing?")
        x()
        print("JOHN: From her case? How could I?")
        x()
        print("YOU: Her phone. Where’s her mobile phone. No phone on the body, no phone in her case. We know she has one - the number’s right there, and you just texted it.")
        x()
        print("JOHN: Maybe she left it at home.")
        x()
        print("YOU: She has a string of lovers, and she’s careful about it - she never leaves it at home.")
        x()
        print("JOHN: So why did I send that text?")
        x()
        print("YOU: The question is, where is that phone now?")
        x()
        print("JOHN: She could’ve lost it.")
        x()
        print("YOU: Yes. Or?")
        x()
        print("JOHN: ... the murderer? You think the murderer has the phone?")
        x()
        print("YOU: Maybe she left it in his car, when she left her case. Maybe he took it for some other reason. Either way, the balance of probability is that the murderer has her phone.")
        x()
        print("JOHN: Sorry, what are we doing here. Did we just text a murderer? What good does that do?")
        x()
        print("As if on cue, John's phone begins to ring. John snatches it up and looks at the number on the sceen. His eyes go to the post-it note with Jennifer Wilson's number on it.")
        x()
        print("YOU:A few hours since his last victim - and now he’s got a text which can only be from her ... Now someone who’d just found the phone would ignore a text like that. But the murderer -")
        x()
        print("The phones stops ringing.")
        x()
        print("YOU: - would panic.")
        x()
        print("You jump off the couch and begin to put on your trenchcoat.")
        x()
        print("JOHN: Have you talked to the police?")
        x()
        print("YOU: Four people are dead - there isn’t time to talk to the police.")
        x()
        print("JOHN: Then why are you talking to me?")
        x()
        print("YOU: Mrs. Hudson took my skull.")
        x()
        print("John looks to the mantlepiece. The skull that was sitting there before is indeed gone.")
        x()
        print("JOHN: So I am basically filling in for your skull?")
        x()
        print("YOU: Relax, you’re doing fine. Well?")
        x()
        print("JOHN: Well what?")
        x()
        print("YOU: Well you could just sit here and watch telly ...")
        x()
        print("John rises to his feet, unsure what his role is.")
        x()
        print("JOHN: You want me to come with you?")
        x()
        print("YOU: I prefer company when I go out - I think better aloud, and the skull just attracts attention.")
        x()
        print("You walk out of your flat. John hesitates, but quickly follows.")
        x()

    def scene_6():
        """"Scene 6 of the game begins when this function is called"""
        #the following prints and the x() function is called to continue the story
        print("A few hours later, you are back in your flat laying on the couch on your back. You had just texted John to come to the flat as soon as possible. After you had left Lauriston Gardens, you searched the area for the pink suitcase belonging to Jennifer Wilson. You had found it, and it was sitting open on your coffee table. Inside the case you expected to find her phone, but did not. The murderer probably had her phone still.")
        x()
        print("Eventually John walks through the door.")
        x()
        print("JOHN: What are you doing?")
        x()
        print("YOU: Nicotine patch, helps me think! Impossible to sustain a smoking habit in London these days - bad news for brain work!")
        x()
        print("JOHN: Good news for breathing.")
        x()
        print("YOU: Oh, breathing - breathing’s boring.")
        x()
        print("JOHN (stepping closer to look at you arm): Three patches??")
        x()
        print("YOU: It’s a three patch problem.")
        x()
        print("You continue to lay on the couch, looking at the ceiling.")
        x()
        print("JOHN: Well?")
        x()
        print("You continue to stare at the ceiling.")
        x()
        print("JOHN: You asked me to come. I’m assuming it’s important.")
        x()
        print("YOU: Oh, yes, of course. Can I borrow your phone?")
        x()
        print("JOHN ... my phone!")
        x()
        print("YOU: Don't want to use mine - always a chance the number’ll be recognised. It’s on my website.")
        x()
        print("JOHN: Mrs. Hudson’s got a phone.")
        x()
        print("YOU: Yes, but she's downstairs. I tried shouting, she didn't hear me.")
        x()
        print("JOHN: I was on the other side of London!!")
        x()
        print("YOU: There was no hurry.")
        x()
        print("John sighs loudly, reaches into his jacket pocket and pulls out his phone, holding it out to you.")
        x()
        print("JOHN: What's this about? The case?")
        x()
        print("YOU: Her case.")
        x()
        print("JOHN: Her case?")
        x()
        print("YOU: Her suitcase, yes, obviously! The murderer took her suitcase. The first big mistake.")
        x()
        print("JOHN: Okay, he took the case. So?")
        x()
        print("You had an idea on how to find the killer, but it was risky.")
        x()
        print("YOU: ... it's no use. There's no other way. We'll just have to risk it.")
        x()
        phone = input("Do you want to take the phone from John or have John text for you? Enter: 'me' or 'john'")
        #the above variable takes the user's input
        phone_possibilities = ["me", "john"]
        #the above list contains the acceptable inputs for the variable phone
        while phone.lower() not in phone_possibilities:
            #this while loop will ask the user the phone variable while their input is not in the phone_possibilities list
            phone = input("Do you want to take the phone from John or have John text for you? Enter: 'me' or 'john'")
        if phone.lower() == "me":
            #if the user's input to phone is "me", the following prints and the x() function is called to continue the story
            print("YOU: There's a number on a post-it on my desk. Hand it to me.")
            x()
            print("John walks over to the desk and retrieves the post-it for you.")
            x()
            print("JOHN: Jennifer Wilson? That was ... hang on, wasn’t that the dead woman?")
            x()
            print("YOU: Yes. Bring me the number.")
            x()
            print("John bring you the number. You send a text that says, 'What happened at Lauriston Gardens? I must have blacked out. 22 Northumberland Street. Please come.'")
            x()
            #the found_suitcase() function is called
            found_suitcase()
        elif phone.lower() == "john":
            #the following prints and the x() function is called to continue the story is the user's input to phone is "john"
            print("YOU: There’s a phone number on my desk - I want you to send a text.")
            x()
            print("JOHN: You brought me here to send a text.")
            x()
            print("YOU: A text, yes! Number on the desk!")
            x()
            print("You look over at John who remains standing still.")
            x()
            print("YOU: What's wrong?")
            x()
            print("JOHN: ... I just met a friend of yours.")
            x()
            print("You were confused. You didn't have any friends.")
            x()
            print("YOU: A friend?")
            x()
            print("JOHN: An enemy.")
            x()
            print("You wondered who he could be talking about. After all, you did have many enemies.")
            x()
            print("Oh! Which one?")
            x()
            print("JOHN: An arch enemy - according to him. Do you have arch enemies?")
            x()
            print("YOU: ...did he offer you money to spy on me?")
            x()
            print("JOHN: Yes.")
            x()
            print("YOU: Did you take it?")
            x()
            print("JOHN: No.")
            x()
            print("YOU: Pity. We could've split the fee. Think it through the next time.")
            x()
            print("JOHN: Who is he?")
            x()
            print("YOU: The most dangerous man you’ve ever met and not my problem, right now. On my desk, the number!")
            x()
            print("John walks over to the desk and grabs the phone number.")
            x()
            print("JOHN: Jennifer Wilson? That was ... hang on, wasn’t that the dead woman?")
            x()
            print("YOU: Yes, doesn’t matter, just enter the number. Are you doing it?")
            x()
            print("JOHN: Yes --")
            x()
            print("YOU: Have you done it?")
            x()
            print("JOHN: Hang on, yes.")
            x()
            print("YOU: Now these words exactly. 'What happened at Lauriston Gardens? I must have blacked out. 22 Northumberland Street. Please come.'")
            x()
            print("JOHN: ...you blacked out?")
            x()
            print("YOU: What? No, no. Type and send, quickly.")
            x()
            print("YOU (after a few moments): Sent it yet?")
            x()
            print("JOHN: Yes.")
            x()
            #the found_suitcase() function is called
            found_suitcase()

    scene_6()

    def scene_7():
        """"Scene 7 of the game begins when this function is called"""
        #the following prints and the x() functions is called to continue the story
        print("You and John both leave the flat and walk to a shabby-looking Italian restaurant on Northumberland Street. You stared across the street at 22 Northumberland Street, the address you texted to Jennifer Wilson’s phone. Later in the night, you saw a taxi stopped outside of 22 Northumberland. You ran through the streets of London with John following closely behind after the taxi. When you caught up to the taxi, you were able to see that the man riding in the taxi had recently arrived from the U.S.; he had an alibi and couldn’t have been the killer.")
        x()
        print("However, when you arrive back at your flat, you are greeted with a startled Mrs. Hudson. She informs you that Lestrade, Anderson, Sally and other members of the police department are upstairs in your flat. Lestrade found out that you had found Jennifer Wilson’s suitcase. Because he couldn’t break into your flat, he disguised entering your flat as a drugs bust.")
        x()
        print("Back at your flat...")
        x()
        print("LESTRADE: Keep looking guys! (to you) Or you could start helping me properly, and I’ll stand them down.")
        x()
        print("YOU: This is childish.")
        x()
        print("LESTRADE: I'm dealing with a child. Sherlock, this is our case! I’m letting you in, but you don’t go off on your own - clear?")
        x()
        print("YOU: What, so you set up a pretend drugs bust, to bully me?")
        x()
        print("LESTRADE: Stops being pretend if they find anything.")
        x()
        global friendship_lestrade
        if friendship_lestrade < 4:
            #if the user's friendship level with lestrade is less than 4, the following prints
            print("Because your friendship level was to low, Lestrade eventually came up with a way to have you arrested. The case was never solved. You have failed.")
            x()
            restart = input("Would you like to go back to the crime scene and restart? Enter: 'y' or 'n'.")
            #the above variable takes the user's input
            while restart.lower() not in ["yes", "y", "no", "n"]:
                #this while loop continues to ask the user the restart variable while their input is not in the above list
                restart = input("Would you like to restart? Enter: 'y' or 'n'.")
            if restart.lower() in ["yes", "y"]:
                #if the user's input to restart is "y" or "yes", scene_1() function is called
                scene_1()
            elif restart.lower() in ["no", "n"]:
                #if the user's input to restart is "n" or "no", the game ends (using sys.exit())
                print("Goodbye.")
                sys.exit()
        elif friendship_lestrade >= 4:
            #if the user's frienship level with lestrade is greater than or equal to 4, the following prints and the x() function is called to continue the story
            print("YOU: I'm clean")
            x()
            print("LESTRADE: Is your flat? All of it?")
            x()
            print("YOU (pulling up your sleeve to show you nicotine patches): I don't even smoke!")
            x()
            print("LESTRADE (also pulling up his sleeve, showing his patch): Neither do I! So let’s work together. We’ve found Rachel.")
            x()
            print("YOU: ... who is she?")
            x()
            print("LESTRADE: Jennifer Wilson’s only daughter.")
            x()
            print("YOU: Her daughter. Why would she write her daughter’s name, why?")
            x()
            print("ANDERSON: Never mind that, we found the case. (At Sherlock) According to someone the murderer has the case - and here it is, in the hands of our favourite psychopath.")
            x()
            print("YOU: I'm not a psychopath, Anderson - I'm a high-functioning sociopath. Do your research!")
            x()
            #the fifth quote is made from the quotes class
            quote_5 = quote("I'm not a psychopath, Anderson - I'm a high-functioning sociopath.", "Sherlock")
            #the fifth quote is introduced to the user using the introduce method from the quotes class
            quote_5.introduce()
            #the fifth quote is added to the quotes list
            quotes.append("I'm not a psychopath, Anderson - I'm a high-functioning sociopath. ~Sherlock")
            x()
            #the following prints and the x() function is called to continue the story
            print("YOU (to Lestrade) You need to bring Rachel in, you need to question her. I need to question her -")
            x()
            print("LESTRADE: She’s dead.")
            x()
            print("YOU: How? When? Is there a connection? There has to be!")
            x()
            print("LESTRADE: I doubt it, since she’s been dead for fourteen years. Technically she was never alive. Rachel was Jennifer Wilson’s still born daughter fourteen years ago.")
            x()
            print("YOU: No. No, that’s not right. Why would she do that?")
            x()
            print("ANDERSON: Why would she think of her daughter in the her last moments. Yeah, sociopath, seeing it now.")
            x()
            print("YOU: She didn’t think about her daughter, she scratched her name on the floor. She was dying, it took effort, it would’ve hurt - she was trying to tell us something!")
            x()
            print("You began pacing frantically.")
            x()
            print("YOU: Yes, but listen! If you were dying, if you'd been murdered, in your very last seconds, what would you say?")
            x()
            print("JOHN: Please God let me live.")
            x()
            print("YOU: Yes, but if you were clever, if you were very clever...Jennifer Wilson, running all those lovers. She was clever, and she's telling us something!")
            x()
            print("Mrs. Hudson enters the flat.")
            x()
            print("MRS. HUDSON: Isn't the doorbell working? Your taxi's here, Sherlock.")
            x()
            print("YOU: I didn't order a taxi, go away.")
            x()
            print("YOU: Shut up! Everybody shut up, I’m thinking, don’t move, don’t breathe, Anderson, face the other way, you’re putting me off!")
            x()
            print("ANDERSON: What, my face is?")
            x()
            print("LESTRADE: Everybody quiet and still. Anderson, turn your back.")
            x()
            print("You stood in the center of the room with your hands on your head thinking as hard as you could until it suddenly hit you.")
            x()
            print("YOU: Oh, she was clever. Clever, yes, I love her! She’s cleverer than you lot dead! Do you see? Do you get it? She didn’t lose her phone, she never lost it. She planted in on him. When she got out that car, she knew she was going to her death - she left the phone to lead us to her killer!")
            x()
            print("LESTRADE: But how?")
            x()
            print("YOU: What do you mean, how? Rachel, don’t you see? Rachel!! Oh, look at you lot, you’re all so vacant! What’s it like, not being me, it must be so relaxing. Rachel is not a name.")
            x()
            #the sixth quote is made from the quote class
            quote_6 = quote("What's it like, not being me, it must be so relaxing.", "Sherlock")
            #the sixth quote is introduced to the user by using the introduce method of the quotes class
            quote_6.introduce()
            #the sixth quote is added to the quotes list
            quotes.append("What's it like, not being me, it must be so relaxing. ~Sherlock")
            #the following prints and the x() function is called to continue the story
            x()
            print("JOHN: Then what is it?")
            x()
            print("You run over to your computer and open a broweser.")
            x()
            print("YOU: John, the luggage label, it had an email address on it.")
            x()
            print("JOHN (reading the luggage tag): Jennie dot pink at mephone dot org dot uk.")
            x()
            print("YOU: I’ve been too slow, she didn’t have a laptop, which means did her business on her phone. So it’s a smartphone, it’s email enabled. So there’s a website for her account.")
            x()
            print("YOU (typing rapidly): The user name will be the email address, and all together now, the password is ... ?")
            x()
            print("JOHN: Rachel.")
            x()
            print("ANDERSON: So we can read her emails - so what?")
            x()
            print("YOU: Don’t talk out loud, Anderson, you lower the IQ of the whole street. We can do more than read her emails - it’s a smartphone, it’s got GPS. And if you lose it, you can locate it online.")
            x()
            #the seventh quote is made from the quotes class
            quote_7 = quote("Don't talk out loud, Anderson, you lower the IQ of the whole street.", "Sherlock")
            #the seventh quote is introduced to the user from the introduce method of the quote class
            quote_7.introduce()
            #the seventh quote is added to the quotes list
            quotes.append("Don't talk out loud, Anderson, you lower the IQ of the whole street. ~Sherlock")
            #the following prints and the x() function is called to continue the story
            x()
            print("YOU: She’s leading us right to the man who killed her.")
            x()
            print("The computer was in the process of locating the phone.")
            x()
            print("LESTRADE: Unless he got rid of it.")
            x()
            print("JOHN: We know he didn’t.")
            x()
            print("YOU:  Get some vehicles ready, get a helicopter, we need to move fast - that phone battery won’t last forever.")
            x()
            print("LESTRADE: We’ll just have a map reference, not a name!")
            x()
            print("YOU: It's a start!")
            x()
            print("JOHN (looking at the computer screen): Sherlock - ")
            x()
            print("YOU (to Lestrade): It narrows it down from anyone in London, it’s the first proper lead we’ve had.")
            x()
            print("JOHN (staring at the computer screen): Sherlock!")
            x()
            print("YOU: Where is it?")
            x()
            print("You run over to the screen and frown. How could that be...?")
            x()
            print("JOHN: It’s here. It’s in 221 Baker Street.")
            x()
            print("YOU: But it can’t be. How can it be here? How??")
            x()
            print("LESTRADE: Maybe it was in the case when you brought it back - fell out somewhere.")
            x()
            print("YOU: And I didn't notice. Me? I didn't notice.")
            x()
            print("JOHN: Anyway, we texted it and he phoned us back.")
            x()
            print("LESTRADE: Guys, we’re also looking for a mobile somewhere here - belonged to the victim ...")
            x()
            print("YOU (thinking to yourself): Who do we trust even if we don't know them?")
            x()
            print("YOU (thinking to yourself): Who passes unnoticed wherever they go?")
            x()
            print("YOU (thinking to yourself): Who hunts in the middle of a crowd?")
            x()
            print("You are about to be asked if you know who the murderer is. This is your last chance to figure out who the murderer is. If you respond 'n', the game will end.")
            #"taxi driver" is added to the possible_murderers list
            possible_murderers.append("taxi driver")
            #the functions murderer() is called
            murderer()
            print("The end.")

    #the function scene_7() is called
    scene_7()
else:
    #the following prints and the game ends
    print("Goodbye.")