import pandas as pd
def delete(file_path, Date_to_remove, Country_Region_to_remove):
    file_path = './full_grouped.csv'
    # Đọc dữ liệu từ file CSV vào DataFrame
    df = pd.read_csv(file_path)

    # Lọc dữ liệu, loại bỏ các dòng có Date và Country/Region cần xóa
    df = df[(df['Date'] != Date_to_remove) | (df['Country/Region'] != Country_Region_to_remove)]

    # Lưu lại DataFrame vào file CSV sau khi đã xóa dòng
    df.to_csv(file_path, index=False)

    print("Hàng đã được xóa thành công!")

if __name__ == "__main__":
    Date_to_remove = input('Nhập date muốn xóa: ')
    Country_Region_to_remove = input('Nhập Region/Country muốn xóa: ')
    file_path = input("Nhập file path: ")
    delete(file_path,Date_to_remove, Country_Region_to_remove)
