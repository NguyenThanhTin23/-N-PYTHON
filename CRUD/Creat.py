import pandas as pd
def creat(file_path):
    #Nhập thông tin dòng mới
    Date = input('Nhập date (yyyy-mm-dd): ')
    Country_Region = input('Nhập Country/Region: ')
    Confirmed = int(input('Nhập số lượng ca dương tính đã được xác nhận (Confirmed): '))
    Deaths = int(input('Nhập số lượng ca tử vong (Deaths): '))
    Recovered = int(input('Nhập số ca đã khỏi bệnh (Recovered): '))
    Active = Confirmed-Deaths-Recovered
    New_cases = int(input('Nhập số lượng trường hợp mới (New cases): '))
    New_deaths = int(input('Nhập số lượng ca tử vong mới (New deaths): '))
    New_recovered = int(input('Nhập số lượng ca dương tính mới(New recovered): '))
    WHO_Region = input('Nhập WHO_Region: ')
    new = [Date,Country_Region,Confirmed,Deaths,Recovered,Active,New_cases,New_deaths,New_recovered,WHO_Region]
    #Đọc dữ liệu file csv vào DataFrame
    df=pd.read_csv(file_path)
    #Tạo dòng mới
    new_row=pd.Series(new,index=df.columns)
    #Thêm dòng mới vào DataFrame
    df.loc[len(df)]=new_row
    #Lưu lại DataFrame vào file csv
    df.to_csv(file_path,index=False)
    print("Dòng mới đã được thêm vào.")
