from collections import Counter

from src.data_loader import load_questions

import numpy as np


def course_distribution():
    questions = load_questions()

    courses = [
        question.course
        for question in questions
    ]

    counts = Counter(courses)

    return counts





def difficulty_statistics():
    questions = load_questions()

    difficulties = np.array([
        question.difficulty
        for question in questions
    ])

    return {
        "mean": float(np.mean(difficulties)),
        "std": float(np.std(difficulties)),
        "min": int(np.min(difficulties)),
        "max": int(np.max(difficulties))
    }




if __name__ == "__main__":
    print("Course distribution:")
    print(course_distribution())

    print()

    print("Difficulty statistics:")
    print(difficulty_statistics())