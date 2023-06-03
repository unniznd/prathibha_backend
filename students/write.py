import csv
from .models import Students

def write_data_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            admission_number = int(row[0])
            student_name = row[1]
            student_branch_id = int(row[2])
            phone_number = row[3]

            # Create the Student object and save it
            student = Students(
                admission_number=admission_number,
                student_name=student_name,
                student_branch_id=student_branch_id,
                phone_number=phone_number,
            )
            student.save()

