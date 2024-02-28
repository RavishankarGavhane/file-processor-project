import csv
import logging
import os
from typing import List, Dict, Any, Tuple


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Reads data from a file and returns it as a list of dictionaries.

    Parameters:
        file_path (str): The path to the input file.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing the data read from the file.
    """
    data = []
    try:
        # Open the file and read data using the CSV DictReader
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for row in reader:
                data.append(row)
        logger.info(f"Successfully read data from {file_path}")
    except Exception as e:
        # Log an error if reading data fails
        logger.error(f"Error reading data from {file_path}: {e}")
    return data


def process_data(data: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], int, float, int, float]:
    """
    Processes the input data and calculates the second highest salary, average salary, highest salary, 
    and highest salary count.

    Parameters:
        data (List[Dict[str, Any]]): A list of dictionaries containing the input data.

    Returns:
        Tuple[List[Dict[str, Any]], int, float, int, float]: A tuple containing processed data, 
        second highest salary, average salary, highest salary, and highest salary count.
    """
    processed_data = []
    gross_salaries = []

    try:
        # Process each entry in the input data
        for entry in data:
            # Calculate gross salary by adding basic salary and allowances
            basic_salary = float(entry.get('basic_salary', 0))  # default to 0 if key not found
            allowances = float(entry.get('allowances', 0))  # default to 0 if key not found
            gross_salary = basic_salary + allowances
            entry['Gross Salary'] = gross_salary  # Add gross salary to the entry
            processed_data.append(entry)  # Append processed entry to the list
            gross_salaries.append(gross_salary)  # Append gross salary to the list

        # Calculate the second highest salary
        sorted_salaries = sorted(gross_salaries, reverse=True)
        second_highest_salary = sorted_salaries[1] if len(sorted_salaries) > 1 else None

        # Calculate the average salary
        average_salary = sum(gross_salaries) / len(gross_salaries) if gross_salaries else None

        # Calculate the highest salary and highest salary count
        highest_salary = max(gross_salaries, default=None)
        highest_salary_count = gross_salaries.count(highest_salary)

        logger.info("Data processing completed successfully")
    except Exception as e:
        # Log an error if data processing fails
        logger.error(f"Error processing data: {e}")
        return [], None, None, None, None

    return processed_data, second_highest_salary, average_salary, highest_salary, highest_salary_count



def write_to_csv(data: List[Dict[str, Any]], output_file: str, second_highest_salary: int, average_salary: float, highest_salary: float, highest_salary_count: int) -> None:
    """
    Writes the processed data to a CSV file along with additional footer information.

    Parameters:
        data (List[Dict[str, Any]]): A list of dictionaries containing the processed data.
        output_file (str): The path to the output CSV file.
        second_highest_salary (int): The second highest salary.
        average_salary (float): The average salary.
        highest_salary (float): The highest salary.
        highest_salary_count (int): The count of employees with the highest salary.
    """
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Sort data by 'Gross Salary' in descending order
        sorted_data = sorted(data, key=lambda x: x['Gross Salary'], reverse=True)

        # Get fieldnames from the first entry of sorted data
        fieldnames = list(sorted_data[0].keys()) if sorted_data else []

        # Add additional fields for footer
        fieldnames += ['Second Highest Salary', 'Average Salary', 'Highest Salary', 'Highest Salary Count']

        # Open the output file and initialize a CSV DictWriter
        with open(output_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Write header row with additional fields
            writer.writeheader()

            # Write additional information to the CSV file
            writer.writerow({'Second Highest Salary': second_highest_salary, 
                             'Average Salary': average_salary, 
                             'Highest Salary': highest_salary,
                             'Highest Salary Count': highest_salary_count})

            # Write each entry in the processed data to the CSV file
            writer.writerows(sorted_data)
        
        logger.info(f"Results written to {output_file} successfully")
    except Exception as e:
        # Log an error if writing results fails
        logger.error(f"Error writing results to {output_file}: {e}")
