import json


questions = [
    {
        "question": "What is an eigenvalue?",
        "course": "Linear Algebra",
        "topic": "Eigenvalues",
        "difficulty": 2
    },
    {
        "question": "What is a derivative?",
        "course": "Calculus",
        "topic": "Derivatives",
        "difficulty": 1
    },
    {
        "question": "What is a binary search tree?",
        "course": "Data Structures",
        "topic": "Trees",
        "difficulty": 2
    }
]


# Print every question
for item in questions:
    print(item["course"], "-", item["question"])


# Add a new question
new_question = {
    "question": "What is BFS?",
    "course": "Data Structures",
    "topic": "Graphs",
    "difficulty": 2
}

questions.append(new_question)


def show_question(item):
    print("Question:", item["question"])
    print("Course:", item["course"])
    print("Topic:", item["topic"])
    print("Difficulty:", item["difficulty"])


def count_course(questions_list, course):
    count = 0

    for item in questions_list:
        if item["course"] == course:
            count += 1

    return count


print()
show_question(questions[0])

print()
print("Data Structures questions:",
      count_course(questions, "Data Structures"))


# Load questions from our JSON dataset
print("\nQuestions loaded from JSON:")

with open("data/raw/questions.json", "r", encoding="utf-8") as file:
    loaded_questions = json.load(file)

for item in loaded_questions:
    print(item["course"], "-", item["question"])