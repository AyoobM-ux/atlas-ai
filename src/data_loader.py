import json

from src.config import RAW_DATA_DIR
from src.data_models import Question


def load_questions() -> list[Question]:
    file_path = RAW_DATA_DIR / "questions.json"

    with open(file_path, "r", encoding="utf-8") as file:
        raw_questions = json.load(file)

    questions = [
        Question(**item)
        for item in raw_questions
    ]

    return questions


if __name__ == "__main__":
    questions = load_questions()

    for question in questions:
        print(question)