import pandas as pd
import matplotlib.pyplot as plt

def plot_monthly_new_cases(file_path, save_path):
    # Đọc dữ liệu từ tệp CSV
    data = pd.read_csv(file_path)

    # Chuyển đổi cột 'Date' thành kiểu datetime
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

    # Nhóm dữ liệu theo tháng và tính tổng số ca mới ('New cases')
    data['Month'] = data['Date'].dt.to_period('M')  # Tạo cột 'Month' với định dạng tháng/năm
    monthly_cases = data.groupby('Month')['New cases'].sum()
    # Vẽ biểu đồ cột
    plt.figure(figsize=(10, 6))
    plt.bar(monthly_cases.index.astype(str), monthly_cases, color='#8B0000')

    # Thêm tiêu đề và nhãn cho các trục
    plt.title('Monthly New COVID-19 Cases (Jan 2020 - Jul 2020)', fontsize=16)

    # Di chuyển tên trục lên trên và thay đổi đơn vị trục Y
    plt.xlabel('Month', fontsize=12, labelpad=10, loc='center')
    plt.ylabel('New Cases', fontsize=12, labelpad=10)


    # Xoay nhãn tháng để dễ đọc
    plt.xticks(rotation=30)

    # Lưu biểu đồ thành ảnh
    plt.tight_layout()
    plt.savefig(save_path)

    print(f"Chart saved to {save_path}")

# Gọi hàm với đường dẫn tệp dữ liệu và đường dẫn lưu ảnh
file_path = 'statistics_data.csv'
save_path = 'static/monthly_chart.png'
plot_monthly_new_cases(file_path, save_path)
