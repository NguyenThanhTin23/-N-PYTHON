import pandas as pd

def delete(file_path,data,rows_to_delete):
    """
    Xóa bản ghi cụ thể trong tệp CSV
    
    :param file_path: str
    :param data: DataFrame
    :param rows_to_delete: list
    :return: None
    """
    data = data.drop(rows_to_delete).reset_index(drop=True)
    # Lưu lại dữ liệu đã xóa vào tệp CSV
    data.to_csv(file_path, index=False)
delete()
