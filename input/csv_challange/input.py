import pathlib , csv

path_file = pathlib.Path.cwd()
scores_file = path_file / "scores.csv"
scores = [{"name": "LLCoolDave", "score":"23"},
          {"name": "LLCoolDave", "score":"27"},
          {"name": "red", "score":"12"},
          {"name": "LLCoolDave", "score":"26"},
          {"name": "tom123", "score":"26"}]
with scores_file.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "score"])
    writer.writeheader()
    writer.writerows(scores)

with scores_file.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    empty = [row for row in reader]
