import random
def run_flashcard():
    print("Welcome")
    print("Type q to quit")

    #Dictionary for flashcards
    vocabulary = {
        "学生 (xuéshēng)": "student",
        "电脑 (diànnǎo)": "computer",
        "喝   (Hē)": "drink",
        "不客气 (Bù kèqì)" : "You are welcome"
    }
    score = 0
    total_asked = 0

    #Converting dictionary to list for it to work
    word_list = list(vocabulary.keys())
    random.shuffle(word_list)

    while True:
        current_word = random.choice(word_list)
        current_translation = vocabulary[current_word]
        print(current_word)

        #Ask the question
        print(f"What is the English translation of {current_word}?")
        user_guess = input("Your answer:").lower()

        #Exit scenerio
        if user_guess == "q":
            break

        #Check answer

        if user_guess not in vocabulary:
            print("Wrong answer")

        else:
            user_guess = current_word.lower()
            score += 1
            total_asked += 1
