from pathlib import Path

path = Path()

FOLDERS = {
    "tmp": path.absolute() / "src" / "app" / "infra" / "tmp",
    "certificates": path.absolute() / "certificates",
}
