import pandas as pd
def delete(file_path, Date_to_remove, Country_Region_to_remove):
    """
    Chức năng:
    Hàm xóa các dòng có giá trị trùng với cột 'Date' và 'Country/Region'. 

    Tham số:
    file_path (str): Đường dẫn đến file CSV cần xử lý.
    Date_to_remove (str): Giá trị cụ thể của cột 'Date' cần loại bỏ.
    Country_Region_to_remove (str): Giá trị cụ thể của cột 'Country/Region' cần loại bỏ.
    
    """
    # Đọc dữ liệu từ file CSV vào DataFrame
    df = pd.read_csv(file_path)

    # Chuyển đổi ngày được nhập thành kiểu datetime
    Date_to_remove = pd.to_datetime()

    # Lọc dữ liệu, loại bỏ các dòng có Date và Country/Region cần xóa
    df = df[(df['Date'] != Date_to_remove) | (df['Country/Region'] != Country_Region_to_remove)]

    # Lưu lại DataFrame vào file CSV sau khi đã xóa dòng
    df.to_csv(file_path, index=False)
