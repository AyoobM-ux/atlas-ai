from dataclasses import dataclass


@dataclass
class Question:
    question: str
    course: str
    topic: str
    difficulty: int
