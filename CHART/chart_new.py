import matplotlib.pyplot as plt
import pandas as pd
def plot_monthly_trends(file_path, save_path):
    df = pd.read_csv(file_path)
    # Chuyển đổi cột 'Date' thành kiểu datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

    # Thêm cột tháng để nhóm dữ liệu
    df['Month'] = df['Date'].dt.to_period('M')

    columns_to_sum = ['New cases', 'New deaths', 'New recovered']
    monthly_data = df.groupby('Month')[columns_to_sum].sum()

    # Vẽ biểu đồ
    plt.figure(figsize=(14, 7))
    plt.plot(monthly_data.index.astype(str), monthly_data['New cases'], label='New Cases', color='blue', marker='o')
    plt.plot(monthly_data.index.astype(str), monthly_data['New deaths'], label='New Deaths', color='red', marker='o')
    plt.plot(monthly_data.index.astype(str), monthly_data['New recovered'], label='New Recovered', color='green', marker='o')

    # Cấu hình biểu đồ
    plt.title('Monthly Trends of COVID-19 Cases, Deaths, and Recoveries', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Case', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.tight_layout()
    plt.savefig(save_path)

    print(f"Chart saved to {save_path}")

file_path = 'statistics_data.csv'
save_path = 'static/monthly_new_chart.png'
plot_monthly_trends(file_path, save_path)
