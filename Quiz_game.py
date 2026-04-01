import random

def run_quiz():
    questions = [
        {
            "question": "What is the capital city of Kenya?",
            "choices": {"A": "Mombasa", "B": "Kisumu", "C": "Nairobi", "D": "Eldoret"},
            "answer": "C"
        },
        {
            "question": "How many colors does the rainbow have?",
            "choices": {"A": "5", "B": "6", "C": "7", "D": "8"},
            "answer": "C"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "choices": {"A": "Mars", "B": "Saturn", "C": "Jupiter", "D": "Neptune"},
            "answer": "C"
        },
    ]

    random.shuffle(questions)

    score = 0
    total = len(questions)
    valid_choices = {"A", "B", "C", "D"}

    print("WELCOME TO THE QUIZ GAME!")
    print(f"\nYou will be asked {total} questions.")
    print("Enter A, B, C, or D for your answer.\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}/{total}: {q['question']}")
        for letter, choice in q["choices"].items():
            print(f"  {letter}. {choice}")

        while True:
            try:
                user_answer = input("\nYour answer: ").strip().upper()
                if user_answer not in valid_choices:
                    raise ValueError("Invalid input")
                break
            except ValueError:
                print("Invalid input! Please enter A, B, C, or D.")

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}. {q['choices'][q['answer']]}\n")

    percentage = (score / total) * 100

    print("\nQUIZ COMPLETE!")
    print(f"\nYour Score: {score}/{total} ({percentage:.0f}%)")

    if percentage >= 80:
        print("Excellent!")
    elif percentage >= 50:
        print("Good job!")
    else:
        print("Try Again!")

    print("\nThanks for playing!")

run_quiz()
