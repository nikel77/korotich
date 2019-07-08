#1. Create .csv file and write all this rows and header there
#2. Given the workers list, create the list of managers

workers_list = [
   {'name': 'Lisa', 'age': 30, 'gender': 'f', 'position': 'Accountant'},
   {'name': 'Mike', 'age': 45, 'gender': 'm', 'position': 'Manager'},
   {'name': 'Nick', 'age': 25, 'gender': 'm', 'position': 'Office Manager'},
   {'name': 'Vera', 'age': 21, 'gender': 'f', 'position': 'Support Manager '},
   {'name': 'Masha', 'age': 33, 'gender': 'f', 'position': 'Accountant'},
   {'name': 'Igor', 'age': 50, 'gender': 'm', 'position': 'Manager'},
   {'name': 'John', 'age': 25, 'gender': 'm', 'position': 'Support'},
   {'name': 'Silvia', 'age': 38, 'gender': 'f', 'position': ' Support Manager'},
   {'name': 'Robert', 'age': 31, 'gender': 'm', 'position': 'Head of department'}
]


def csv_creator(data):
    import csv

    with open('people.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';')
        filewriter.writerow(data[0].keys())
        for row in data:
            filewriter.writerow([row['name'], row['age'], row['gender'], row['position']])
    managers_list = [row for row in data if 'Manager' in row['position']]
    return managers_list


print(csv_creator(workers_list))


def csv_creator1(data):
    import csv

    with open('people.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';')
        filewriter.writerow(['name', 'age', 'gender', 'position'])
        managers_list = []
        for row in data:
            filewriter.writerow([row['name'], row['age'], row['gender'], row['position']])
            if 'Manager' in row['position']:
                managers_list.append(row)
    return managers_list


print(csv_creator1(workers_list))
