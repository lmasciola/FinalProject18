def x():
    x = input("")
    return x

clues = []
places = []

play = input("INTRUCTIONS: Welcome to the game. In this game, you play as the infamous detective Sherlock Holmes. After every line of dialogue, press enter to continue. Would you like to play?")
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

    print("Lestrade wouldn't be here unless something was different this time.")
    x()

    print("YOU: What's different about this one? You wouldn't have come to get me if there wasn't anything new.")
    x()
else:
    print("Goodbye.")