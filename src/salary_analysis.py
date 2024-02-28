import csv

def process_file(file_path):
    data = []
    salaries = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        header = next(reader)  # Skip the header row
        for row in reader:
            data.append(row)
            salary = float(row[5])  # Assuming salary is in the 6th column (index 5)
            salaries.append(salary)

    # Calculate second highest salary
    sorted_salaries = sorted(salaries, reverse=True)
    second_highest_salary = sorted_salaries[1] if len(sorted_salaries) > 1 else None

    # Calculate highest salary count
    highest_salary = sorted_salaries[0]
    highest_salary_count = sorted_salaries.count(highest_salary)

    # Calculate average salary
    average_salary = sum(salaries) / len(salaries)

    return data, second_highest_salary, highest_salary_count, average_salary, len(data)

def main():
    # Process each file
    file_paths = [
        r"C:\Users\Sonam Gavhane\Downloads\file_processor_project\data\DATA.dat",
        r"C:\Users\Sonam Gavhane\Downloads\file_processor_project\data\DATA1.dat"
    ]

    for file_path in file_paths:
        data, second_highest_salary, highest_salary_count, average_salary, num_rows = process_file(file_path)
        print(f"For file {file_path}:")
        print("Data:")
        for row in data:
            print(row)
        print(f"Second Highest Salary: {second_highest_salary}")
        print(f"Highest Salary Count: {highest_salary_count}")
        print(f"Average Salary: {average_salary}")
        print(f"Number of rows: {num_rows}")
        print()

if __name__ == "__main__":
    main()
