import pandas as pd

def delete(file_path,data,rows_to_delete):
    """
    Chức năng: 
    Xóa các hàng trong Data theo index được lưu trong rows_to_delete, 
    sau đó đặt lại index của Data để đảm bảo rằng index được đánh số liên tục

    :param file_path: str
    :param data: DataFrame
    :param rows_to_delete: list
    :return: None
    """
    # Xóa bản ghi và đặt lại index một cách liên tục
    data = data.drop(rows_to_delete).reset_index(drop=True)

    # Lưu lại dữ liệu đã xóa vào tệp CSV
    data.to_csv(file_path, index=False)
