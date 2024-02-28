# main.py
import logging
from file_processor import read_data, process_data, write_to_csv

def main() -> None:
    """
    Main function to process input files, perform data processing, and write results to an output file.

    Reads data from multiple input files, processes the data to calculate statistics,
    and writes the results to an output CSV file.
    """
    # List of file paths to input data files
    file_paths = [
        'data/data.dat',     # Path to the first input data file
        'data/data1.dat'     # Path to the second input data file
    ]

    try:
        # Initialize an empty list to store all data from input files
        all_data = []

        # Read data from each file and append to the all_data list
        for path in file_paths:
            file_data = read_data(path)
            all_data.extend(file_data)
            logging.info(f"Successfully read {len(file_data)} entries from {path}")

        # Process all data to calculate statistics
        processed_data, second_highest_salary, average_salary, highest_salary, highest_salary_count = process_data(all_data)
        
        # Path to the output CSV file
        output_file = 'output/result.csv'

        # Write processed data and additional footer information to the output CSV file
        write_to_csv(processed_data, output_file, second_highest_salary, average_salary, highest_salary, highest_salary_count)

        # Print additional information to the console
        print("Second Highest Salary:", second_highest_salary)
        print("Average Salary:", average_salary)
        print("Highest Salary:", highest_salary)
        print("Highest Salary Count:", highest_salary_count)

    except Exception as e:
        # Log an error if any exception occurs
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
