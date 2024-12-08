import pandas as pd

# Load dữ liệu từ file CSV
def day(data,start_date,end_date):
     """
     Lọc dữ liệu theo khoảng thời gian và tính tổng số liệu hằng ngày.

     Parameters:
     -----------
     data : pandas.DataFrame
          DataFrame chứa dữ liệu với các cột bắt buộc:
          - 'Date': Ngày (định dạng dd/mm/yyyy)
          - 'New cases': Số ca nhiễm mới mỗi ngày
          - 'New deaths': Số ca tử vong mới mỗi ngày
          - 'New recovered': Số ca hồi phục mới mỗi ngày
     start_date : str
          Ngày bắt đầu (định dạng dd/mm/yyyy).
     end_date : str
          Ngày kết thúc (định dạng dd/mm/yyyy).

     Returns:
     --------
     pandas.DataFrame
          DataFrame chứa tổng số ca nhiễm, tử vong, và hồi phục mới theo từng ngày trong khoảng thời gian.

     """
     data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
     start_date = pd.to_datetime(start_date, format='%d/%m/%Y')
     end_date = pd.to_datetime(end_date, format='%d/%m/%Y')
     date_range_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

     daily_totals = date_range_data.groupby('Date')[['New cases', 'New deaths', 'New recovered']].sum().reset_index()

     return daily_totals




       
