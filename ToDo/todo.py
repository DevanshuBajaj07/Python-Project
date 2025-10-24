def ask_question(question, options, correct_option):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= len(options):
                return answer == correct_option
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Please enter a number.")

def load_questions():
    """Load questions from a data source (e.g., file, database, or hardcoded)."""
    return [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_option": 3
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_option": 2
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
            "correct_option": 2
        }
    ]

def play_quiz(questions):
    """Play the quiz game with the given questions."""
    score = 0
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_option"]):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    return score

def display_score(score, total_questions):
    """Display the final score to the user."""
    print(f"\nYour final score is: {score}/{total_questions}")
    print("Thanks for playing!")

def main():
    print("Welcome to the Quiz Game!")
    questions = load_questions()
    score = play_quiz(questions)
    display_score(score, len(questions))

if __name__ == "__main__":
    main()