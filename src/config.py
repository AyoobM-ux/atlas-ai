from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = PROJECT_ROOT / "models"


def show_paths():
    print("Project root:", PROJECT_ROOT)
    print("Raw data:", RAW_DATA_DIR)
    print("Processed data:", PROCESSED_DATA_DIR)
    print("Models:", MODEL_DIR)


if __name__ == "__main__":
    show_paths()