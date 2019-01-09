clues = []
#this is the list of clues the player will use to help them solve the mystery
quotes = []
#this is the list of funny quotes the player may discover during the episode

def x():
    """Players to read text one line at a time and press enter to read the next line of text. The player will also be able to type the word 'clues' to see the list of clues they have so far."""
    x = input("")
    if x == "":
        return x
    elif x.lower() == "clues":
        print(clues)
        x = input("")
class quote:
    """Class defining famous/funny quotes from the episode"""
    def __init__(self, quote, person):
        """Constructor for quote class"""
        self.quote = quote
        self.person = person
    def introduce(self):
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

play = input("INTRUCTIONS: Welcome to the game. In this game, you play as the infamous detective Sherlock Holmes. (THIS GAME IS BASED OFF OF THE EPISODE OF BBC SHERLOCK A STUDY IN PINK, AND USES DIALOGUE FROM THE SHOW).After every line of text, press enter to continue or type 'clue' to view your current list of clues. Would you like to play?")
#this take the user input and asks the player if they want to play the game
if play.lower() == "yes" or play.lower() == "y":
#if the player inputs "yes" or "y" the game will start
    def scene_1():
        """"Scene one of the game begins when this function is calles"""
        #the story begins. lines of text are printed one by one for the player to read. the player presses enter after every line to get to the next line of text. in between lines of code, the player can type 'clues' to view their list of clues'
        print("Introduction:")
        print("Your name is Sherlock Holmes, an infamous detective. You live in London in 221B Baker Street with Dr. John Watson. You are sitting in your flat when Mrs. Hudson, your landlady, asks you your opinion about the recent suicides that have been reported in the paper.")
        x()
        print("MRS. HUDSON: What about these suicides, then, Sherlock? Thought that would be right up your street. Three of them, exactly the same. That's a bit funny, isn't it?")
        x()
        print("You suddenly get a feeling.")
        x()
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
        #the first clue is created based on the clue class. the clue description is listed first in the parentheses followed by the location the clue was found
        clue_1 = clue("Fourth Suicide Note", "Lauriston Gardens")
        #this is a method from the clue class that introduces/describes the first clue found to the player
        clue_1.introduce()
        #this clue is added to the clues list. now when the player wants to look at their list of clues, this clue will be in the list
        clues.append("The Fourth Suicide left a note")
        #the story is continued by printing lines of text followed by the previously definied command x()
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
    #this calls the previously defined scene_1() function
    scene_1()
    def assistant_john():
        """This function continues the story when the player picks John as their assistant to take to the crime scene."""
        #the story is continued by printing lines of text followed by the previously defined function x()
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
        print("You and John run out of the flat. You hail a cab and climb inside, telling the cabbie to head to Lauriston Gardens.")
    def scene_2():
        """Scene 2 will begin when this function is called"""
        assistant_decision = input("You put on your black trench coat and blue scarf and dash out the door. You stop outside the door after exiting the flat. You should get going, but you need an assistant. Who should you ask to be you assistant? Mrs. Hudson or John Watson?")
        #this takes the user input of who they want to take to the crime scene with them
        possible_assistants = ["john watson", "mrs. hudson"]
        #this is the list of acceptable inputs when the player is prompted with the previously defined assistant_decision
        while assistant_decision.lower() not in possible_assistants:
            #this is a while loop that continues to ask for the player's input until their input for assistant_decision matches one of the options in possible_assistants
            assistant_decision = input("You put on your black trench coat and blue scarf and dash out the door. You stop outside the door after exiting the flat. You should get going, but you need an assistant. Who should you ask to be you assistant? Mrs. Hudson or John Watson?")
        if assistant_decision.lower() == "mrs. hudson":
            #the following will happen if the user's input to assistant_decision is 'mrs. hudson'
            print("She probably wouldn't do well at a crime scene.")
            take_hudson = input("Are you sure you want to bring Mrs. Hudson? Enter: 'yes' or 'no.'")
            #this asks for the user's input on if they are sure they want to take Mrs. Hudson to the crime scene
            if take_hudson.lower() == "y" or take_hudson.lower() == "yes":
                #if the user's input for take_hudson is 'yes' or 'y', a string will be printed telling the player they have failed
                print("You take Mrs. Hudson to the crime scene. She wasn't that helpful. The case was never solved. You have failed.")
                restart = input("Would you like to go back to the last scene and restart? y or n?")
                #this takes the user input on whether or not they want to restart the game after they have failed by bringing Mrs. Hudson to the crime scene
                if restart.lower() == "y" or restart.lower() == "yes":
                    #if the user's input to restart is 'yes' or 'y', scene_2() is called and the game will continue from the beginning of the function scene_2()
                    scene_2()
                elif restart.lower() == "n" or restart.lower() == "no":
                    print("Goodbye.")
            elif take_hudson.lower() == "no" or take_hudson.lower() == "n":
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
        quote_1 = quote("I'm a consulting detective. Only one in the world. I invented the job.", "Sherlock Holmes")
        quote_1.introduce()
        quotes.append("I'm a consulting detective. Only one in the world. I invented the job. ~Sherlock Holmes")
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
        quote_2 = quote("You were thinking. It's annoying.", "Sherlock Holmes")
        quote_2.introduce()
        quotes.append("You were thinking. It's annoying. ~Sherlock Holmes")
        examining = True
        options_examine = ["hand", "coat", "jewelry", "leg"]
        while examining:
            examine = input(f"You move closer to the body to examine it. Where do you want to examine? {', '.join(options_examine)}")
            while examine.lower() not in options_examine:
                examine = input(f"You move closer to the body to examine it. Where do you want to examine? {', '.join(options_examine)}")
            if examine.lower() == "hand":
                print("With her left hand, Wilson had scratched word into the floorboards. The word is 'Rache.'")
                x()
                print("'Rache' means 'revenge' in German.")
                x()
                print("You think for a moment...")
                x()
                print("Rachel.")
                x()
                clue_2 = clue("Jennifer scratched the word 'RACHE' into the floorboards. You believe she didn't finish and was instead writing 'Rachel'", "Lauriston Gardens")
                clue_2.introduce()
                clues.append("Jennifer Wilson scratched 'Rachel' into the floorboards")
                x()
                print("You look at Wilson's fingernails. All were painted pink to match her coat and heels. The only nails chip were those she used to carve into the wooden floor.")
                clue_5 = clue("Jennifer Wilson does not work with her hands", "Lauriston Gardens")
                clue_5.introduce()
            elif examine.lower() == "coat":
                print("You run your gloved hand over the woman's coat. The coat was wet.")
                x()
                print("You pull a fold-away umbrella out of her coat pocket. It was dry.")
                x()
                print("You run your hand under the collar of the woman's coat. The collar is wet.")
                clue_3 = clue("Jennifer Wilson was outside in a windy rain storm", "Lauriston Gardens")
                clue_3.introduce()
                clues.append("Jennifer Wilson was outside in a rain storm prior to her death.")
            elif examine.lower() == "jewelry":
                print("You examine the woman's left hand. The woman was wearing her wedding ring. Unlike all of her other jewelry, her wedding ring was dirty.")
                clue_4 = clue("Jennifer Wilson was unhappily married", "Lauriston Gardens")
                clue_4.introduce()
                clues.append("Jennifer Wilson was unhappily married.")
                x()
                print("You take off Wilson's wedding ring. While the outside is dirty, the inside is clean like her other jewelry, meaning the ring is regularly removed. You believe that Wilson was probably an adulter whose lovers did not know she was married.")
                clue_6 = clue ("Jennifer Wilson was an adulterer", "Lauriston Gardens")
                clue_6.introduce()
                clues.append("Jennifer Wilson was an adulterer.")
            elif examine.lower() == "leg":
                print("You look at the back of Wilson's right leg. It is covered in small splashes, probably from a suitcase she was carrying.")
                clue_7 = clue("Wilson had a suitcase with her", "Lauriston Gardens")
                clue_7.introduce()
                clues.append("Wilson had a suitcase with her.")
            options_examine.remove(examine)
            if len(options_examine) == 0:
                examining = False
    scene_4()
    def scene_5():
        print("LESTRADE: Got anything?")
        x()
        print("YOU: Not much.")
        x()
        print("Anderson walks in. He works with the police department.")
        x()
        print("She's German. Rache is German for revenge. She could be trying to tell us something.")
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
        print("YOU: The wedding ring, ten years old at least. The rest of her jewellery has been regularly cleaned, but not her wedding rings - state of her marriage, right there. The inside of the rings are shinier than the outside - that means they’re regularly removed; the only polishing they get is when she works them off her finger. It’s not for work - look at her nails, she doesn’t work with her hands - so what, or rather who, does she remove her rings for? Clearly not one lover - she’d never sustain the fiction of being single over time - so more likely a string of them. Simple!")
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
        quote_3 = quote("Dear God, what's it like in your funny little brains? It must be so boring.", "Sherlock Holmes")
        quote_3.introduce()
        quotes.append("Dear God, what's it like in your funny little brains? It must be so boring. ~Sherlock Holmes")
        x()
        print("YOU: It’s slightly damp - she’s been in heavy rain within the last few hours. No rain anywhere in London in that time. Under her coat collar is damp too. She turned it up against the wind! She’s got an umbrella in her left pocket but it’s unused and dry. Not just wind, strong wind - too strong to use her umbrella.We know from her suitcase that she’s staying over night so she must have a come a decent distance. But she can’t have travelled more than two or three hours, cos her coat hasn’t dried. So where has there been heavy rain and strong wind within the radius of that travel time? Cardiff.")
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
        print("YOU: No, she was leaving an angry note in German - of course she was writing Rachel. No other word it can be. Question is, why did she wait till she was dying to write it...")
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
        print("You shove past Lestrade and stride onto the landing of the stairs.")
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
        print("YOU: She never made it to her hotel. Look at her hair - colour coordinates her lipstick and her shoes, she’d never have left a hotel with her hair still like --")
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
        print(quotes)
    scene_5()
else:
    print("Goodbye.")