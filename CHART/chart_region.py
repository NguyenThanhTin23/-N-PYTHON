import pandas as pd
import matplotlib.pyplot as plt

def plot_monthly_region_cases(file_path, save_path):
    # Đọc dữ liệu từ tệp CSV
    df = pd.read_csv(file_path)

    # Chuyển đổi cột 'Date' thành kiểu datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

    # Tạo cột 'Month' từ cột 'Date'
    df['Month'] = df['Date'].dt.to_period('M')

    # Lấy danh sách các vùng độc nhất
    regions = df['WHO Region'].unique()

    # Tính số lượng trục cần thiết (nếu có nhiều hơn 6 vùng, sẽ cần thêm trục)
    rows = (len(regions) + 2) // 3  # Tính toán số hàng cần thiết
    cols = 3  # 3 cột

    # Thiết lập lưới biểu đồ
    fig, axes = plt.subplots(rows, cols, figsize=(10, 3 * rows), sharex=True, sharey=True)
    axes = axes.flatten()

    # Các cột cần vẽ
    columns_to_plot = ['Confirmed', 'Deaths', 'Recovered']

    # Màu sắc cho từng loại dữ liệu
    color_palette = {'Confirmed': 'blue', 'Deaths': 'red', 'Recovered': 'green'}

    # Vẽ biểu đồ mật độ cho từng vùng theo tháng
    for i, region in enumerate(regions):
        region_data = df[df['WHO Region'] == region]

        # Tính tổng số ca bệnh theo tháng
        monthly_data = region_data.groupby('Month')[columns_to_plot].sum().reset_index()

        # Vẽ biểu đồ mật độ cho từng cột
        for category in columns_to_plot:
            axes[i].plot(monthly_data['Month'].astype(str), monthly_data[category], label=category, color=color_palette[category])
            axes[i].fill_between(monthly_data['Month'].astype(str), monthly_data[category], alpha=0.5, color=color_palette[category])
            axes[i].tick_params(axis='x', rotation=20)
        axes[i].set_title(region, fontsize=10)  # Giảm kích thước tiêu đề
        axes[i].set_xlabel('Month', fontsize=8)
        axes[i].set_ylabel('Cases', fontsize=8)
        axes[i].legend(fontsize=8, loc='upper left')  # Đảm bảo hiển thị legend đúng

    # Tối ưu hóa bố cục
    plt.tight_layout(pad=2)  # Giảm khoảng cách giữa các biểu đồ
    plt.suptitle('Density Plots for WHO Regions by Month', fontsize=12, y=1.001)  # Giảm kích thước tiêu đề tổng
    
    # Lưu biểu đồ thành ảnh
    plt.savefig(save_path)

    print(f"Chart saved to {save_path}")

# Gọi hàm với đường dẫn tệp dữ liệu và đường dẫn lưu ảnh
file_path = 'data_dirty.csv'  # Đường dẫn tệp dữ liệu của bạn
save_path = 'static/region_monthly_chart.png'  # Đường dẫn lưu ảnh
plot_monthly_region_cases(file_path, save_path)
