def x():
    x = input("")
    return x

clues = []
places = []

play = input("INTRUCTIONS: Welcome to the game. In this game, you play as the infamous detective Sherlock Holmes. (THIS GAME IS BASED OFF OF THE EPISODE OF BBC SHERLOCK< A STUDY IN PINK, AND USES DIALOGUE FROMT THE SHOW).After every line of dialogue, press enter to continue. Would you like to play?")
if play.lower() == "yes" or play.lower() == "y":
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

    assistant_decision = input("You put on your black trench coat and blue scarf and dash out the door. You stop outside the door after exiting the flat. You should get going, but you need an assistant. Who should you ask to be you assistant? Mrs. Hudson or John Watson?")
    if assistant_decision.lower() == "mrs. hudson":
        print("She probably wouldn't do well at a crime scene. You should ask John.")
    elif assistant_decision.lower() == "john watson":
        print("Good choice. You head back inside to speak to John.")

else:
    print("Goodbye.")