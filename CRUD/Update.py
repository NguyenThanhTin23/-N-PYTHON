import csv
def update():
    Date = input('Nhập date (yyyy-mm-dd): ') #chuẩn hóa theo định dạng yyyy-mm-dd nếu user nhập sai
    Country_Region = input('Nhập Country/Region: ')
    Confirmed = int(input('Nhập số lượng ca dương tính đã được xác nhận (Confirmed): '))
    Deaths = int(input('Nhập số lượng ca tử vong (Deaths): '))
    Recovered = int(input('Nhập số ca đã khỏi bệnh (Recovered): '))
    Active = int(input('Nhập số lượng người dương tính (Active): '))
    New_cases = int(input('Nhập số lượng trường hợp mới (New cases): '))
    New_deaths = int(input('Nhập số lượng ca tử vong mới (New deaths): '))
    New_recovered = int(input('Nhập số lượng ca dương tính mới(New recovered): '))
    WHO_Region = input('Nhập WHO_Region: ')
    data = [Date,Country_Region,Confirmed,Deaths,Recovered,Active,New_cases,New_deaths,New_recovered,WHO_Region]

    # data_input = input("Nhập dữ liệu (Date,Country_Region,Confirmed,Deaths,Recovered,Active,New_cases,New_deaths,New_recovered,WHO_Region): \n")
    # data = data_input.split(',')
    file_path = './full_grouped.csv'
    with open(file_path, "a", newline = '') as fd:
        csv_writer = csv.writer(fd, delimiter=',')
        csv_writer.writerow(data)
    print('Update thành công!')
if __name__ == "__main__":
    update()