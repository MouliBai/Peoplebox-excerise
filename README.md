# Peoplebox-excerise 1
# Transforming Employee Data into Historical Versioning Format

This Python script transforms employee data from one format to another, organizing it into a historical versioning format.

## Description

This script reads employee data from a CSV file and transforms it into a new CSV format. It consolidates multiple records for each employee, based on different dates such as compensation dates, review dates, and engagement dates.

## Requirements

- Python 3.x
- Required Python packages: `csv`, `datetime`, `os`

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository or download the script file (`Transforming employee data into a historical versioning format.py`) to your local machine.
3. Prepare your input CSV file with employee data. Ensure it follows the required format.
4. Update the `input_file` variable in the script to point to your input CSV file.
5. Run the script using the following command:

# Transforming Employee Data into Historical Versioning Format

This Python script transforms employee data from one format to another, organizing it into a historical versioning format.

## Input Format

The input CSV file should contain employee data with the following columns:

- Employee Code
- Manager Employee Code
- Date of Joining
- Date of Exit (optional)
- Compensation
- Compensation 1
- Compensation 1 date
- Compensation 2
- Compensation 2 date
- Review 1
- Review 1 date
- Review 2
- Review 2 date
- Engagement 1
- Engagement 1 date
- Engagement 2
- Engagement 2 date

## Output

The script generates a new CSV file named `output.csv` containing transformed employee data. The output CSV file will have the following columns:

- Employee Code
- Manager Employee Code
- Effective Date
- End Date
- Compensation
- Compensation 1
- Compensation 2
- Review 1
- Review 2
- Engagement 1
- Engagement 2

## License
This project is licensed under the MIT License - see the LICENSE file for details.
```vbnet
You can directly paste this content into your README.md file. Let me know if you need any further assistance!

mailto: baimouli@gmail.com


