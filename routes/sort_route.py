from flask import Blueprint, request, render_template
from routes.paginate import paginate_data
import pandas as pd
from FEATURE.Sort_df import sorted_dt

file_path = 'data_dirty.csv' 
sort_file_path = 'FEATURE/sort.csv'

data = pd.read_csv(file_path) 
ROWS_PER_PAGE = 12
sort_bp = Blueprint('sort', __name__, url_prefix='/sort')
@sort_bp.route('/sort', methods=['GET', 'POST'])
def sort_data():
    column = request.args.get('column', 'Date')
    order = request.args.get('order', 'asc')  # Mặc định là sắp xếp tăng dần
    page = int(request.args.get('page', 1))
    
    # Đọc dữ liệu từ file CSV
    data = pd.read_csv(file_path)

    sortData = sorted_dt(data, column, order)
    # Phân trang dữ liệu đã sắp xếp
    sortData.to_csv(sort_file_path, index=False)
    ROWS_PER_PAGE = 10
    pagination = paginate_data(sortData, page, ROWS_PER_PAGE)
    
    # Hiển thị dữ liệu trên giao diện
    return render_template(
        'sort.html',
        table_data=pagination["table_data"],
        headers=sortData.columns,
        page=page,
        total_pages=pagination["total_pages"],
        has_next=pagination["has_next"],
        has_prev=pagination["has_prev"],
        nearby_pages=pagination["nearby_pages"],
        current_sort={'column': column, 'order': order}
    )