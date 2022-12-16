import csv    
with open('python.csv', mode='w') as csv_file:    
    fieldnames = ['emp_name', 'dept', 'birth_month']    
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)    
    writer.writeheader()    
    writer.writerow({'emp_name': 'Parker', 'dept': 'Accounting', 'birth_month': 'November'})    
    writer.writerow({'emp_name': 'Smith', 'dept': 'IT', 'birth_month': 'October'})    
