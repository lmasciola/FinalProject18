def x():
    x = input("")
    return x

clues = []
places = []

play = input("INTRUCTIONS: Welcome to the game. In this game, you play as the infamous detective Sherlock Holmes. (THIS GAME IS BASED OFF OF THE EPISODE OF BBC SHERLOCK A STUDY IN PINK, AND USES DIALOGUE FROM THE SHOW).After every line of text, press enter to continue. Would you like to play?")
if play.lower() == "yes" or play.lower() == "y":
    def scene_1():
        print("Introduction:")
        print("Your name is Sherlock Holmes, an infamous detective. You live in London in 221B Baker Street with Dr. John Watson. You are sitting in your flat when Mrs. Hudson, your landlady, asks you your opinion about the recent suicides that have been reported in the paper.")
        x()
        print("MRS. HUDSON: What about these suicides, then, Sherlock? Thought that would be right up your street. Three of them, exactly the same. That's a bit funny, isn't it?")
        x()
        print("You suddenly get a feeling.")
        print("YOU: Four. There's been a fourth. And there's something different this time.")
        x()
        print("MRS. HUDSON: A fourth? How do you know?")
        x()
        print("You look out the window to see the blue light of a police car parked below. You hear feet thumping on the stairs. In comes Lestrade, a detective from the local police force who often uses you as a consultant.")
        x()
        print("YOU: Where?")
        x()
        print("LESTRADE: Brixton. Lauriston Gardens.")
        x()
        places.append("Lauriston Gardens")
        print("You have just discovered a new place, Lauriston Gardens.")
        x()
        print("Lestrade wouldn't be here unless something was different this time.")
        x()
        print("YOU: What's different about this one? You wouldn't have come to get me if there wasn't anything new.")
        x()
        print("LESTRADE: You know how they never leave notes?")
        x()
        print("YOU: Yeah.")
        x()
        print("LESTRADE: This one did. Will you come?")
        x()
        clues.append("Fourth victim left note")
        print("You have just discovered a clue: the fourth suicide left a note.")
        x()
        print("You think for a moment. There were a few people who worked at the police department that disliked you.")
        x()
        print("YOU: Who's on Forensics?")
        x()
        print("LESTRADE: Anderson.")
        x()
        print("YOU: Anderson won't work with me.")
        x()
        print("LESTRADE: He won't be your assistant.")
        x()
        print("YOU: But I need an assistant.")
        x()
        print("LESTRADE: Will you come?")
        x()
        print("YOU: Not in a police car. I'll be right behind you.")
        x()
        print("LESTRADE: Thank you!")
        x()
        print("Lestrade left and headed to Lauriston Gardens.")
        x()
        print("YOU: Brilliant! And I thought it was going to be a boring evening. Serial suicides, and now a note. Mrs. Hudson, I'll be late -- might need some food.")
        x()
        print("MRS. HUDSON: I'm your landlady, dear, not your housekeeper.")
        x()
        print("YOU: Something cold is fine. John, make yourself at home -- have a cuppa! Don't wait up!")
    scene_1()
    def assistant_john():
        print("You walk back inside the flat.")
        x()
        print("YOU: You're a doctor.")
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
        print("You and John run out of the flat. You hail a cab and climb inside, telling the cabbie to head to Lauriston Gardens.")
    def scene_2():
        assistant_decision = input("You put on your black trench coat and blue scarf and dash out the door. You stop outside the door after exiting the flat. You should get going, but you need an assistant. Who should you ask to be you assistant? Mrs. Hudson or John Watson?")
        possible_assistants = ["john watson", "mrs. hudson"]
        while assistant_decision not in possible_assistants:
            assistant_decision = input("You put on your black trench coat and blue scarf and dash out the door. You stop outside the door after exiting the flat. You should get going, but you need an assistant. Who should you ask to be you assistant? Mrs. Hudson or John Watson?")
        if assistant_decision.lower() == "mrs. hudson":
            print("She probably wouldn't do well at a crime scene.")
            sure = input("Are you sure you want to bring Mrs. Hudson?")
            if sure.lower() == "y" or sure.lower() == "yes":
                print("You take Mrs. Hudson to the crime scene. She wasn't that helpful. The case was never solved. You have failed.")
                restart = input("Would you like to go back to the last scene and restart? y or n?")
                if restart.lower() == "y" or restart.lower() == "yes":
                    x()
                    scene_2()
                elif restart.lower() == "n" or restart.lower() == "no":
                    print("Goodbye.")
            elif sure.lower() == "no" or sure.lower() == "n":
                print("You should ask John.")
                assistant_john()
        elif assistant_decision.lower() == "john watson":
            print("Good choice. You head back inside to speak to John.")
            assistant_john()
    scene_2()
    def question_1_answer():
        print("YOU: I'm a consulting detective. Only one in the world. I invented the job.")
        x()
        print("JOHN: What does that mean?")
        x()
        print("YOU: It means that when the police are out of their depth - which is always - they consult me.")
        x()
    def scene_3():
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
        question_1 = input("How would you like to answer? Enter: consulting detective OR sassy remark.")
        if question_1.lower() == "consulting detective":
            question_1_answer()
        elif question_1.lower() == "sassy remark":
            print("YOU: What do you think?")
            x()
            print("JOHN: I'd say you were a private detective, but --")
            x()
            print("YOU: But?")
            x()
            print("JOHN: The police doesn't go to priavte detectives.")
            x()
            question_1_answer()
    #scene_3()
else:
    print("Goodbye.")