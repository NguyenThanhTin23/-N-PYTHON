import pandas as pd
from datetime import datetime
def country(data,start_date,end_date):
      
     """
     Lọc dữ liệu COVID-19 trong khoảng thời gian xác định và lấy thông tin ngày cuối cùng 
     của từng quốc gia trong khoảng đó, sau đó sắp xếp theo số ca nhiễm giảm dần.

     Parameters:
     -----------
     data : pandas.DataFrame
          DataFrame chứa dữ liệu COVID-19 với các cột bắt buộc:
          - 'Date': Ngày (định dạng dd/mm/yyyy)
          - 'Country/Region': Tên quốc gia
          - 'Confirmed': Số ca nhiễm
          - 'Deaths': Số ca tử vong
          - 'Recovered': Số ca hồi phục
     start_date : str
          Ngày bắt đầu (định dạng dd/mm/yyyy).
     end_date : str
          Ngày kết thúc (định dạng dd/mm/yyyy).

     Returns:
     --------
     pandas.DataFrame
          DataFrame chứa thông tin của các quốc gia với số liệu tại ngày cuối cùng trong khoảng thời gian,
          được sắp xếp giảm dần theo số ca nhiễm.

     """
     data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
     start_date = datetime.strptime(start_date, '%d/%m/%Y')
     end_date = datetime.strptime(end_date, '%d/%m/%Y')
     filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]
     # Để lấy dữ liệu của ngày cuối cùng cho từng quốc gia, ta lấy ngày cuối cùng của mỗi quốc gia trong khoảng thời gian đã lọc
     latest_data = filtered_data.sort_values('Date').groupby('Country/Region')[['Country/Region','Confirmed','Deaths','Recovered']].tail(1)
     # Sắp xếp theo số ca nhiễm giảm dần  
     latest_data = latest_data.sort_values(by='Confirmed', ascending=False)
     return latest_data



