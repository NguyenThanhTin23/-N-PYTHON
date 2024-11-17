import pandas as pd
def read(file_path):
    """
    Chức năng:
    Đọc dữ liệu file CSV

    Tham số:
    file_path(str): Đường dẫn file CSV cần đọc
    """
    df=pd.read_csv(file_path)
    return df
