import pathlib

current_dir = pathlib.Path(__file__).parent
file_name = "salaries.txt"

def total_salary(path: str) -> tuple:
    try:
        with open(path, "r", encoding="utf-8") as file:
            developers_count = 0
            salary_total = 0
            salary_average = 0

            for line in file.readlines():
                normalized_line = line.strip()

                if not normalized_line: # skip empty lines if they are presented
                    continue

                user_data = normalized_line.split(",")
                salary_total += int(user_data[1])
                developers_count += 1

            salary_average = salary_total // developers_count

            return (salary_total, salary_average)
    except FileNotFoundError as e:
        print(f"Error on file open, details: {e}")
        return None

if __name__ == "__main__":
    total, average = total_salary(current_dir / file_name)
    print(f"Total salary: {total}, Average salary: {average}")
