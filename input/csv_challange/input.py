import pathlib 

path_file = pathlib.Path.cwd() / "input" / "csv_challange"
path_file.mkdir(parents = True, exist_ok = True)
source = path_file / ".." / ".." / "input.py"
destination = path_file / "input.py"
source.replace(destination)
