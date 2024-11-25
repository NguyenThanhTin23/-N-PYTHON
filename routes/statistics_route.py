from flask import Blueprint, request, redirect, flash, render_template
from routes.paginate import paginate_data
import pandas as pd
from STATISTICAL.by_country import country
from STATISTICAL.by_day import day
from STATISTICAL.by_region import region
import os

file_path = 'data_dirty.csv' 
stats_file_path = 'STATISTICAL/statistics_data.csv' 
data = pd.read_csv(file_path) 
ROWS_PER_PAGE = 12
statistics_bp = Blueprint('statistics', __name__, url_prefix='/statistics')
@statistics_bp.route('/statistics', methods=['GET', 'POST'])
def statistics():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        stats_type = request.form['stats_type']
        stats_result = None
        if stats_type == 'region':
            stats_result = region(data, start_date, end_date)
        elif stats_type == 'day':
            stats_result = day(data, start_date, end_date)
            stats_result['Date'] = stats_result['Date'].dt.strftime('%d/%m/%Y')
        elif stats_type == 'country':
            stats_result = country(data, start_date, end_date)

        stats_result.to_csv(stats_file_path, index=False)


        # Chuyển hướng đến trang phân trang để xem dữ liệu đã lọc
        return redirect('/statistics/statistics?page=1')

    # Lấy số trang hiện tại từ query params (nếu không có thì mặc định là 1)
    page = int(request.args.get('page', 1))

    # Nếu không có dữ liệu đã lọc, đọc dữ liệu từ file gốc
    if os.path.exists(stats_file_path):
             stats_result = pd.read_csv(stats_file_path)
    else:
        # Nếu không, đọc file gốc
        stats_result = pd.read_csv(file_path)

    # Phân trang dữ liệu
    pagination = paginate_data(stats_result, page, ROWS_PER_PAGE)

    # Hiển thị dữ liệu trên giao diện
    return render_template(
        'statistics.html',
        table_data=pagination["table_data"],
        headers=stats_result.columns,
        page=page,
        total_pages=pagination["total_pages"],
        has_next=pagination["has_next"],
        has_prev=pagination["has_prev"],
        nearby_pages=pagination["nearby_pages"],
    )