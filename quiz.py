


format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

print(f"{format_output}---START---{format_reset}")
print("")


welcome_message = ("WELCOME TO KNOW YOUR ANATOMY QUIZ!")
print(welcome_message)
print("")

Instruction = ("There are 10 questions to answer, In each question choose betweenc option A to D. Only one answer is correct.")
print(f"Instruction: {Instruction}")
print("")


questions = ("Which organ is primarily responsible for pumping blood throughout the human body? ", 
             "What is the largest bone in the human body? ", 
             "Which part of the human body is responsible for producing insulin? ", 
             "How many chambers does the human heart have? ", 
             "What is the primary function of red blood cells? ",
             "What is the smallest bone in the human body? ",
             "Which part of the brain is responsible for coordinating voluntary movements and balance? ",
             "What is the main function of the human lungs? ",
             "Which of the following is the primary function of the kidneys? ",
             "Which type of blood vessel carries blood away from the heart? ",
             )







options = (("A. Brain", "B. Liver", "C. Heart", "D. Brain"),
           ("A. Tibia ", "B. Femur", "C. Humerus", "D. Radius"),
           ("A. Pancreas", "B. Stomach", "C. Kidney", "D. Liver"),
           ("A. Two", "B. Four", "C. Six", "D. Eight"),
           ("A. Fight infection", "B. Produce energy", "C. Carry oxygen", "D. Filter blood"),
           ("A. Stapes", "B. Patella", "C. Ulna", "D. Ribs"),
           ("A. Cerebrum", "B. Medulla", "C. Cerebellum", "D. Thalamus"),
           ("A. Pump blood", "B. Digest food", "C. Produce hormones", "D. Exchange oxygen and carbon dioxide"),
           ("A. Control body temperature", "B. Filter waste from the blood", "C. Store fat", "D. Produce red blood cells"),
           ("A. Artery", "B. Capillary", "C. Vein", "D. Venule")
           )






answers = ("C", "B", "A", "B", "C", "A", "C", "D", "B", "A")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


print("------------------------------")
print("            RESULT            ")
print("-------------------------------")


print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()


print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()


score  = int(score/len(questions) *100)

print(f"Your score is: {score}%")





print("")
print(f"{format_output}---END---{format_reset}")