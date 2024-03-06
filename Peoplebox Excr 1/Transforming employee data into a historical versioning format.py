import csv
from datetime import datetime, timedelta
import os

def transform_data(input_file):
    output_file = os.path.join(os.path.dirname(input_file), 'output.csv')
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    historical_data = []

    for employee in data:
        employee_records = []
        past_record = None

        joining_date = datetime.strptime(employee['Date of Joining'], '%Y-%m-%d').date()
        exit_date = datetime.strptime(employee['Date of Exit'], '%Y-%m-%d').date() if employee['Date of Exit'] else datetime(2100, 1, 1).date()

        compensation_dates = [datetime.strptime(employee['Compensation 1 date'], '%Y-%m-%d').date() if employee['Compensation 1 date'] else None,
                              datetime.strptime(employee['Compensation 2 date'], '%Y-%m-%d').date() if employee['Compensation 2 date'] else None]
        review_dates = [datetime.strptime(employee['Review 1 date'], '%Y-%m-%d').date() if employee['Review 1 date'] else None,
                        datetime.strptime(employee['Review 2 date'], '%Y-%m-%d').date() if employee['Review 2 date'] else None]
        engagement_dates = [datetime.strptime(employee['Engagement 1 date'], '%Y-%m-%d').date() if employee['Engagement 1 date'] else None,
                            datetime.strptime(employee['Engagement 2 date'], '%Y-%m-%d').date() if employee['Engagement 2 date'] else None]

        all_dates = sorted([d for d in [joining_date] + compensation_dates + review_dates + engagement_dates if d is not None])

        for i in range(len(all_dates)):
            effective_date = all_dates[i]
            end_date = all_dates[i + 1] - timedelta(days=1) if i < len(all_dates) - 1 else exit_date

            record = {
                'Employee Code': employee['Employee Code'],
                'Manager Employee Code': employee['Manager Employee Code'],
                'Effective Date': effective_date,
                'End Date': end_date,
                'Compensation': employee['Compensation'] if i == 0 else past_record['Compensation'] if past_record else '',
                'Compensation 1': employee['Compensation 1'] if effective_date == compensation_dates[0] else past_record['Compensation 1'] if past_record else '',
                'Compensation 2': employee['Compensation 2'] if effective_date == compensation_dates[1] else past_record['Compensation 2'] if past_record else '',
                'Review 1': employee['Review 1'] if effective_date == review_dates[0] else past_record['Review 1'] if past_record else '',
                'Review 2': employee['Review 2'] if effective_date == review_dates[1] else past_record['Review 2'] if past_record else '',
                'Engagement 1': employee['Engagement 1'] if effective_date == engagement_dates[0] else past_record['Engagement 1'] if past_record else '',
                'Engagement 2': employee['Engagement 2'] if effective_date == engagement_dates[1] else past_record['Engagement 2'] if past_record else ''
            }

            employee_records.append(record)
            past_record = record

        historical_data.extend(employee_records)

    fieldnames = ['Employee Code', 'Manager Employee Code', 'Effective Date', 'End Date', 'Compensation',
                  'Compensation 1', 'Compensation 2', 'Review 1', 'Review 2', 'Engagement 1', 'Engagement 2']

    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(historical_data)

# accessing input file path
input = r'E:\DataScience Guvi\guvi\Internshala\Peoplebox\input.csv'
# Usage
transform_data(input)