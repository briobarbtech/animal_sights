import csv

def save_data(ubicacion):
    with open('db.csv',mode='w',newline='',encoding='utf-8') as csv_file:
        csv_file_writer = csv.writer(csv_file)
        csv_file_writer.writerow(ubicacion.to_list())
    print(f"El archivo 'db.csv' ha sido guardado correctamente.")

        
def get_data(file_name):
    data= []
    with open(f'{file_name}.csv',mode='r',newline='',encoding='utf-8') as csv_file:
        csv_file_reader = csv.reader(csv_file)

        for i in csv_file_reader:
            data.append(i)
    return data