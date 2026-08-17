from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
MODEL_DIR = PROJECT_ROOT / "models"


def show_path():
    print("Project root:",PROJECT_ROOT)
    print("Data folder :",DATA_DIR)
    print("Models folder:",MODEL_DIR)


if __name__=="__main__":
    show_path()