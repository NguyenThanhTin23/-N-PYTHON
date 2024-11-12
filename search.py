import pandas as pd

def search_csv(file_path, date_to_search, country_region_to_search):
    """
    Hàm tìm kiếm dữ liệu trong file CSV theo hai cột Date và Country/Region.
    file_path: Đường dẫn tới file CSV.
    date_to_search: Giá trị cần tìm kiếm trong cột Date.
    country_region_to_search: Giá trị cần tìm kiếm trong cột Country/Region.
    """
    
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(file_path)
    
    # Loại bỏ khoảng trắng thừa trong tên cột (nếu có)
    df.columns = df.columns.str.strip()
    
    # Tìm kiếm dữ liệu dựa vào điều kiện ở hai cột
    result = df[(df['Date'] == date_to_search) & (df['Country/Region'] == country_region_to_search)]
    
    # Kiểm tra kết quả
    if result.empty:
        print("Không tìm thấy kết quả nào khớp với điều kiện tìm kiếm.")
    else:
        print("Kết quả tìm kiếm:")
        print(result)

if __name__ == "__main__":
    file_path = input("Nhập đường dẫn tới file CSV: ")
    date_to_search = input("Nhập ngày cần tìm trong cột Date: ")
    country_region_to_search = input("Nhập khu vực cần tìm trong cột Country/Region: ")
    search_csv(file_path, date_to_search, country_region_to_search)
