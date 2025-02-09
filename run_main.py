import os.path

from script.main import main
import csv
if __name__ == "__main__":
    csv_file = os.path.join('data.csv')
    base_dir = 'script'


    def read_csv_and_process(csv_file, base_dir):
        try:
            with open(csv_file, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    email = row['email']
                    password = row['password']

                    main(email, password)
        except FileNotFoundError:
            print('File not found')

    read_csv_and_process(csv_file, base_dir)
