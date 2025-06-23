import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
SRC_DIR = BASE_DIR / "src"
ELJUR_DATA_DIR = BASE_DIR / "RESULT"
ELJUR_RECEIVED_DATA_DIR = ELJUR_DATA_DIR / "received"
ELJUR_SENT_DATA_DIR = ELJUR_DATA_DIR / "sent"