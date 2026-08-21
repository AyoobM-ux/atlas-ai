import random

from src.data_loader import load_questions


def split_questions(
    questions,
    train_ratio=0.70,
    validation_ratio=0.15,
    seed=42
):
    questions = questions.copy()

    random.seed(seed)
    random.shuffle(questions)

    total = len(questions)

    train_end = int(total * train_ratio)

    validation_end = train_end + int(
        total * validation_ratio
    )

    train = questions[:train_end]

    validation = questions[
        train_end:validation_end
    ]

    test = questions[validation_end:]

    return train, validation, test


if __name__ == "__main__":
    questions = load_questions()

    train, validation, test = split_questions(questions)

    print("Total:", len(questions))
    print("Train:", len(train))
    print("Validation:", len(validation))
    print("Test:", len(test))