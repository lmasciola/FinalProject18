clues = []
def x():
    x = input("")
    if x == "":
        return x
    elif x.lower() == "clues":
        print(clues)
        x = input("")

places = []
class clue:

    def __init__(self, name, place):
        self.name = name
        self.place = place

    def introduce(self):
        print(f"You have discovered a new clue: {self.name}. This clue was discovered at {self.place}")

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

        clue_1 = clue("Fourth Suicide Note", "Lauriston Gardens")
        clue_1.introduce()
        clues.append("The Fourth Suicide left a note")
        print(clues)

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
        while assistant_decision.lower() not in possible_assistants:
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
    def question_3_answer():
        print("YOU: We are here.")
        x()
        print("You both step out of the cab and begin to walk towards the building in Lauriston Gardens surrounded by police cars.")
    def question_1_answer():
        print("YOU: I'm a consulting detective. Only one in the world. I invented the job.")
        x()
        print("JOHN: What does that mean?")
        x()
        print("YOU: It means that when the police are out of their depth - which is always - they consult me.")
        x()
        print("JOHN: Ah...")
        x()
        print("YOU: When I first met you, I asked Afghanistan or Iraq. You seemed surprised.")
        x()
        print("JOHN: How did you know?")
        question_2 = input("How would you like to answer? Enter 'tell' OR 'later'.")
        possible_question_2 = ['tell', 'later']
        while question_2.lower() not in possible_question_2:
            question_2 = input("How would you like to answer? Enter 'tell' OR 'later'.")
        if question_2.lower() == "tell":
            print("YOU: I didn't know. I saw.")
            x()
            print("YOU: Tanned face --")
            x()
            print("YOU: -- but no tan above the wrists. You've been abroad but not sunbathing.")
            x()
            print("YOU: Your haircut and the way you hold yourself says military - but your conversation as you entered the room says you trained at Barts. So army doctor. Obvious!")
            x()
            print("YOU: Your limp is really bad when you walk, but you don’t ask for a chair when you stand, like you’ve forgotten about it - so it’s at least partly psychosomatic. That says the circumstances of the original injury were traumatising - wounded in action then.")
            x()
            print("YOU: Wounded in action, a suntan. Afghanistan or Iraq?")
            x()
            print("You were being a show off.")
            x()
            show_off = input("Do you want to continue analyzing John? yes or no?")
            possible_show_off = ["yes", "y", "no", "n"]
            while show_off.lower() not in possible_show_off:
                show_off = input("Do you want to continue analyzing John? yes or no?")
            if show_off.lower() == "y" or show_off.lower() == "yes":
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
                print("The engraving reads 'To Harry From Clara xxx'")
                x()
                print("YOU: Harry Watson - clearly a family member who’s given you his old phone. Not your father - this is a young man’s gadget. Could be a cousin, but you’re a war hero who can’t find a place to live - unlikely you’ve got an extended family, certainly not one you’re close to. So - brother it is.")
                x()
                print("YOU: Now Clara, who’s Clara - three kisses says it’s a romantic attachment, the expense of the phone says wife not girlfriend.")
                x()
                print("YOU: She must have given it to him recently, this model’s only six months old. It’s a marriage in trouble then - six months on he’s just given it away. If she’d left him, he’d probably have kept the phone - people do, sentiment - but no, he wanted rid of it: he left her. He gave the phone to you - that says he wants you to stay in touch.")
                x()
                question_3 = input("You have a hunch about Harry. Do you want to mention it to John? Enter: 'yes' or 'no'.")
                possible_question_3 = ["yes", "y", "no", "n"]
                while question_3.lower() not in possible_question_3:
                    question_3 = input("You have a hunch about Harry. Do you want to mention it to John? Enter: 'yes' or 'no'.")
                if question_3.lower() == "y" or question_3.lower() == "yes":
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
                    question_4 = input("Do you want to ask John if you got everything correct? Enter: 'yes' or 'no'.")
                    possible_question_4 = ["yes", "no", "y", "n"]
                    while question_4.lower() not in possible_question_4:
                        question_4 = input("Do you want to ask John if you got everything correct? Enter: 'yes' or 'no'.")
                    if question_4.lower() == "y" or question_4.lower() == "yes":
                        print("YOU: Did I get anything wrong?")
                        x()
                        print("JOHN: Harry and me don’t get on, never have. Clara and Harry split up three months ago, they’re getting a divorce. Harry’s a drinker --")
                        x()
                        print("YOU: Spot on, then! Didn’t expect to be right about everything.")
                        x()
                        print("JOHN: --Harry is short for Harriet")
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
                        question_3_answer()
                    else:
                        question_3_answer()
                elif question_3.lower() == "no" and question_3.lower() == "n":
                    question_3_answer()
            elif show_off.lower() == "n" or show_off.lower() == "no":
                question_3_answer()
        elif question_2.lower() == "later":
            question_3_answer()
    def scene_3():
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
        question_1 = input("How would you like to answer? Enter: 'consulting detective' OR 'sassy remark'.")
        possible_question_1 = ["consulting detective", "sassy remark"]
        while question_1.lower() not in possible_question_1:
            question_1 = input("How would you like to answer? Enter: 'consulting detective' OR 'sassy remark'.")
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
    scene_3()
    def examine_hand():
        print("You examine the woman's left hand. The woman was wearing her wedding ring.")
        clue_2 = clue("Jennifer Wilson is married", "Lauriston Gardens")
        clue_2.introduce()
        clues.append("Jennifer Wilson is married.")
        print("With her left hand, Wilson had scratched word into the floorboards. The word is 'Rache.'")
        x()
        print("'Rache' means 'revenge' in German.")
        x()
        print("You think for a moment...")
        x()
        print("Rachel.")
        x()
        clue_3 = clue("Jennifer scratched the word 'RACHE' into the floorboards. You believe she didn't finish and was instead writing 'Rachel.'", "Lauriston Gardens")
        clue_3.introduce()
        clues.append("Jennifer Wilson scratched 'Rachel' into the floorboards")

    def scene_4():
        print("You and John exited the cab and walked up to the police tape surrounding the building.")
        x()
        print("SALLY: Hello, freak.")
        x()
        print("Sally works at the police department.")
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
        print("SALLY: Freak's here. Bringing him in.")
        x()
        print("Sally brings you and John into the building and upstairs to the second floor. You walk into the room where the crime was committed. Lestrade is there.")
        x()
        print("LESTRADE: Jennifer Wilson, according to her credit cards - we’re running them now for contact details. Hasn’t been here long - some kids found her.")
        x()
        print("A woman in a a bright pink coat, and pink shoes, lies dead, sprawled face down. The room remained silent, but you couldn't think.")
        x()
        print("YOU: Shut up!")
        x()
        print("LESTRADE: Didn't say anything.")
        x()
        print("YOU: You were thinking. It's annoying.")
        x()
        examine_1 = input("""You move closer to the body to examine it. Where do you want to examine?
        -hand
        -coat
        -umbrella
        -jewelry""")
        possible_examine_1 = ["hand", "coat", "umbrella", "jewelry"]
        while examine_1.lower() not in possible_examine_1:
            examine_1 = input("""You move closer to the body to examine it. Where do you want to examine first?
        -hand
        -coat
        -umbrella
        -jewelry""")
        if examine_1.lower() == "hand":
            examine_hand()
            del possible_examine_1[0]
            examine_1 = input("""You move closer to the body to examine it. Where do you want to examine?
        -hand
        -coat
        -umbrella
        -jewelry""")
        #page 41
    scene_4()
else:
    print("Goodbye.")