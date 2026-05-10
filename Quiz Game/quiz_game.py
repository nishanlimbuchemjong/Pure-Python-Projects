import json, os, random

FILE_NAME= 'question.json'

def load_question():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except:
        return []

def save_question(questions):
    with open(FILE_NAME, 'w') as file:
        json.dump(questions, file, indent=4)

def add_question():
    questions = load_question()

    question = input("Enter quesiton: ")
    
    options = []
    for i in range(4):
        opt = input(f"Enter option {i+1}: ")
        options.append(opt)
    
    answer = input("Enter correct answer (option): ")

    new_question ={
        'question': question,
        'options': options,
        'answer': answer
    }

    questions.append(new_question)

    save_question(questions)
    print("New Question added successfully.")

def take_quiz():
    questions = load_question()

    if len(questions) < 10:
        print("Add at least 10 questions.")
        return

    selected_questions = random.sample(questions, 10)

    score = 0
    print("\nQuestions: \n```````````````````````")
    for i, q in enumerate(selected_questions):
        print(f"\nQ.{i+1}. {q['question']}")

        # shuffle options
        options = q['options'].copy()
        random.shuffle(options)

        for idx, opt in enumerate(q['options']):
            print(f"{idx+1}. {opt}")
        print("\n")
        try:
            choice = int(input("Enter your correct option [1-4]: "))
            selected_answer = q['options'][choice-1]

            if selected_answer == q['answer']:
                print("✅ Correct ")
                score += 1
            else:
                print("❌ Incorrect")
        except:
            print("Invalid Input..")
    
    print(f"\nYour Score = {score}/10", )


def main():
    while True:
        print("\n==== QUIZ MENU ====")
        print("1. Add Question")
        print("2. Take Quiz")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_question()
        elif choice == "2":
            take_quiz()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__== '__main__':
    main()
