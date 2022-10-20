from csv import reader,writer


f_file = writer(open("final.csv","w"))

for i in range(6):
    with open(f"Inventory{i+1}.csv","r") as file:
        csv_file = reader(file)
        for entry in csv_file:
            f_file.writerow(entry)