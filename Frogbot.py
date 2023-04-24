import random
print("Welcome to Frog Chatbot. What's on your mind today? *ribbit*")
doExit = False

while doExit == False:
    choice = input()
    if choice == "quit":
        doExit = True
        break

    #listen and respond to feelings
    if choice.find("sad") != -1 or choice.find("feeling down") != -1 or choice.find("upset") != -1 or choice.find("angry") != -1 :
        print("I'm sorry to hear you're feeling that way.")
    elif choice.find("happy") != -1 or choice.find("glad") != -1 or choice.find("excited") != -1 or choice.find("looking forward") != -1 :
        print("That's great!")
    elif choice.find("I'm") != -1: #these next three lines let you repeat the word after "I'm" back in a sentence
        word_list = choice.split() #break the sentence into a list with one word per slot
        next_word = word_list[word_list.index("I'm")+1] #find the word after "I'm"
        if next_word == "a":
            next_word = word_list[word_list.index("a")+1]
            print("Why are you", next_word+ "?")
        else:
            print("Why are you", next_word+ "?") #repeat it back 
        #NOTE: it would be good to add an if statement here checking if the next word was "a" 
        #so if someone says "I'm a frog", it doesn't say back, "Why are you a?"

    #listen and respond to specific topics
    elif choice.find("fly") != -1 or choice.find("cricket") != -1 or choice.find("snails") != -1 or choice.find("worms") != -1 :
        print("MMMM DINNER. *ribbit*")

    elif choice.find("dog") != -1 or choice.find("cat") != -1 or choice.find("fish") != -1 or choice.find("bird") != -1 :
        print("OH! YOU HAVE PET, tell me more... *ribbit*")
        
    elif choice.find("ribbit") != -1 or choice.find("Ribbit") != -1 or choice.find("RIBBIT") != -1:
        print("You are frog? Tell me more, what kind of frog are you? *ribbit*")
    elif choice.find("Bullfrog") != -1 or choice.find ("PotatoFairy") != -1 or choice.find ("Posionous") != -1:
        print("Very cool frog. *ribbit*")
    elif choice.find("Toad") != -1 or choice.find("toad") != -1:
        print("You are not frog, you are toad.")
        
    else: #randomize last statement so it's not too repetetive 
        num = random.randrange(1, 100)
        if num <25:
            print("Can you tell me more?")
        elif num <50:
            print("frog asks, tell me more please. *ribbit*")
        elif num <75:
             print("Why?")
        else:
            print("What does that suggest to you?")
