import csv
def creat():
    Date = input('Nhập date (yyyy-mm-dd): ')
    Country_Region = input('Nhập Country/Region: ')
    Confirmed = int(input('Nhập số lượng ca dương tính đã được xác nhận (Confirmed): '))
    Deaths = int(input('Nhập số lượng ca tử vong (Deaths): '))
    Recovered = int(input('Nhập số ca đã khỏi bệnh (Recovered): '))
    Active = int(input('Nhập số lượng người dương tính (Active): '))
    New_cases = int(input('Nhập số lượng trường hợp mới (New cases): '))
    New_deaths = int(input('Nhập số lượng ca tử vong mới (New deaths): '))
    New_recovered = int(input('Nhập số lượng ca dương tính mới(New recovered): '))
    WHO_Region = input('Nhập WHO_Region: ')
    new_row = [Date,Country_Region,Confirmed,Deaths,Recovered,Active,New_cases,New_deaths,New_recovered,WHO_Region]
    with open('full_grouped.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(new_row)
    print("Dòng mới đã được thêm vào.")
if __name__=="__main__":
    creat()