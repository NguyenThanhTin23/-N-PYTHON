import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import math

# Sử dụng chế độ 'Agg' để lưu biểu đồ thay vì hiển thị
matplotlib.use('Agg')

def plot_covid_pie(data, save_path=None):
    # Lọc dữ liệu (loại bỏ 'theworld' nếu có)
    data = data[data['WHO Region'].str.lower() != 'the world']

    # Trích xuất dữ liệu
    regions = data['WHO Region']
    confirmed = data['Confirmed']

    # Tính toán phần trăm cho từng khu vực
    total_confirmed = confirmed.sum()
    percentages = (confirmed / total_confirmed) * 100

    # Tạo biểu đồ tròn
    plt.figure(figsize=(8, 8))
    color = ['#0A7075','#FF6347','#4169E1','#DC143C','#7CFC00','#8B4513']
    wedges, texts, autotexts = plt.pie(confirmed, startangle=140, colors= color, autopct='%1.1f%%')

    # Thêm tiêu đề xuống dưới và gần vào biểu đồ
    plt.suptitle('Distribution of Confirmed COVID-19 Cases by WHO Region', fontsize=20, va='bottom', ha='center', y=-0.005)

    # Thêm chú thích bên ngoài biểu đồ
    plt.legend(
        handles=wedges, 
        labels=[f"{region}: {percent:.1f}%" for region, percent in zip(regions, percentages)],
        title="Regions",
        loc="center left", 
        bbox_to_anchor=(1, 0.5),  # Đặt legend bên phải hình tròn
        fontsize=12,  # Phóng to bảng mô tả
        title_fontsize=14,  # Phóng to tiêu đề của legend
        borderpad=1.5  # Tăng khoảng cách giữa các mục trong legend
    )

    # Lưu hoặc hiển thị biểu đồ
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Pie chart saved to {save_path}")
    else:
        plt.show()
    plt.close()

# Đường dẫn lưu biểu đồ
pie_chart_path = 'static/chart_region.png'

# Đọc dữ liệu từ file CSV
data = pd.read_csv('statistics_data.csv')

# Gọi hàm vẽ biểu đồ tròn
plot_covid_pie(data, save_path=pie_chart_path)
