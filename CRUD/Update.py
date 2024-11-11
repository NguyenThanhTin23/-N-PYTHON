import pandas as pd
#Mẫu cho list_to_update = [Date,Country_Region,Confirmed,Deaths,Recovered,Active,New_cases,New_deaths,New_recovered,WHO_Region]
def update(file_path, list_to_update):
    # Đọc file CSV vào DataFrame
    df = pd.read_csv(file_path)

    # Cập nhật dữ liệu
    date_to_update = list_to_update[0]
    country_region_to_update = list_to_update[1]
    field_name = ["Date", "Country/Region", "Confirmed", "Deaths", "Recovered",
                    "Active", "New cases", "New deaths", "New recovered", "WHO Region"]

    # Lọc dòng cần cập nhật với cả 2 điều kiện
    condition = (df['Date'] == date_to_update) & (df['Country/Region'] == country_region_to_update)
    
    # Cập nhật các giá trị trong dòng đã tìm thấy
    df.loc[condition, field_name] = list_to_update
    
    # Lưu lại DataFrame vào file CSV
    df.to_csv(file_path, index=False)

    print(f"Đã cập nhật thông tin của {date_to_update} {country_region_to_update} thành công!")

if __name__ == "__main__":
    data_input = input("Nhập dữ liệu (Date,Country_Region,Confirmed,Deaths,Recovered,Active,New_cases,New_deaths,New_recovered,WHO_Region): \n")
    data = data_input.split(',')
    file_path = input('Nhập file_path của csv: ')
    update(file_path, data)
