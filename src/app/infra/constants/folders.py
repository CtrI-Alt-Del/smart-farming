from pathlib import Path

path = Path(__file__).parent.parent

FOLDERS = {
    "tmp": path.absolute() / "tmp",
    "certificates": path.absolute() / "certificates",
}
