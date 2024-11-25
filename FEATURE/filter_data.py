import pandas as pd
from datetime import datetime

def filter_dataframe(data, date_start=None, date_end=None, country=None, region=None):
    """
    Lọc dữ liệu từ DataFrame dựa trên các tiêu chí.
    
    :param data: DataFrame gốc cần lọc.
    :param date_start: Ngày bắt đầu (dạng chuỗi 'dd/mm/yyyy'), hoặc None.
    :param date_end: Ngày kết thúc (dạng chuỗi 'dd/mm/yyyy'), hoặc None.
    :param country: Tên quốc gia (hoặc None).
    :param region: Tên vùng (hoặc None).
    :return: DataFrame đã lọc.
    """
    # Đảm bảo cột 'Date' ở định dạng datetime
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

    # Lọc theo ngày bắt đầu
    if date_start:
        date_start = datetime.strptime(date_start, '%d/%m/%Y')
        data = data[data['Date'] >= date_start]
    
    # Lọc theo ngày kết thúc
    if date_end:
        date_end = datetime.strptime(date_end, '%d/%m/%Y')
        data = data[data['Date'] <= date_end]
    
    # Lọc theo quốc gia
    if country:
        data = data[data['Country/Region'] == country]
    
    # Lọc theo vùng
    if region:
        data = data[data['WHO Region'] == region]
    
    return data
