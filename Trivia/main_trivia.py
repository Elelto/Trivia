import json

def load_quiz(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def display_question(question):
    print(f"קטגוריה: {question['category']}")
    print(f"רמת קושי: {question['difficulty']}")
    print(f"שאלה: {question['question']}")
    for key, answer in question['answers'].items():
        print(f"{key}. {answer}")
    correct = question['correct_answer']
    print(f"תשובה נכונה: {correct}")

def run_quiz():
    questions = load_quiz('questions.json')
    for question in questions['questions']:
        display_question(question)
        print()

if __name__ == "__main__":
    run_quiz()
