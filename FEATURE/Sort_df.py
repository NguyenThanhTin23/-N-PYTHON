import pandas as pd

def sorted_dt(data, sort_by, order='asc'):
    """
    Hàm thực hiện sắp xếp dữ liệu cho DataFrame.

    Args:
        data (pd.DataFrame): DataFrame chứa dữ liệu cần sắp xếp.
        sort_by (str): Tên cột để sắp xếp.
        order (str): 'asc' cho tăng dần, 'desc' cho giảm dần.

    Returns:
        pd.DataFrame: DataFrame đã được sắp xếp.
    """
    # Kiểm tra nếu `order` là 'asc' hoặc 'desc'
    ascending = True if order == 'asc' else False

    # Sắp xếp DataFrame theo cột `sort_by`
    try:
        sorted_data = data.sort_values(by=sort_by, ascending=ascending)
    except KeyError:
        # Nếu cột không tồn tại, trả về DataFrame gốc
        sorted_data = data

    return sorted_data
