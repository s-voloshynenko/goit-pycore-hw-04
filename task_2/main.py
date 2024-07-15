import pathlib

current_dir = pathlib.Path(__file__).parent
file_name = "cats.txt"

def get_cats_info(path: str) -> tuple:
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats = []

            for line in file.readlines():
                normalized_line = line.strip()
                if not normalized_line: # skip empty lines if they are presented
                    continue
                cat_id, name, age = normalized_line.split(",")
                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })

            return cats
    except FileNotFoundError as e:
        print(f"Error on file open, details: {e}")
        return None

if __name__ == "__main__":
    cats_info = get_cats_info(current_dir / file_name)
    print(cats_info)
