from src.data_loader import load_questions


def main():
    print("AtlasAI starting...")

    questions = load_questions()

    print(f"Loaded {len(questions)} questions.")

    for question in questions:
        print(
            question.course,
            "-",
            question.question
        )


if __name__ == "__main__":
    main()