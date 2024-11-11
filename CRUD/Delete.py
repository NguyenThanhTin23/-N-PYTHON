import csv
def delete():
    Date_to_remove = input('Nhập date muốn xóa: ')
    Country_Region_to_remove = input('Nhập Region/Country muốn xóa: ')
    file_path = './full_grouped.csv'
    field_name = ["Date", "Country/Region", "Confirmed", "Deaths", "Recovered",
                    "Active", "New cases", "New deaths", "New recovered", "WHO Region"]

    with open(file_path, 'r', newline='') as infile:
        reader = csv.DictReader(infile,fieldnames=field_name, delimiter=',')
        rows = []
        for row in reader:
            if row['Date'] != Date_to_remove or row['Country/Region'] != Country_Region_to_remove:
                rows.append(row)

    with open(file_path, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile,fieldnames=field_name, delimiter=',')
        writer.writerows(rows)
    
    print("Hàng đã được xóa thành công!")
if __name__ == "__main__":
    delete()