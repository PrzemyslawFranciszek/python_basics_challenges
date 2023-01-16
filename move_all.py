import pathlib
new_dir = pathlib.Path(r"C:\Users\przem\OneDrive\Dokumenty\Python\Python Basics\Challenges\python_basics_challenges\practice_files")
new_folder = new_dir / "images"
new_folder.mkdir()
documents_dir = pathlib.Path.home()
for path in documents_dir.rglob("*.*"):
    if path.suffix.lower() in [".png", ".jpg", ".gif"]:
        path.replace(images_dir / path.name)
