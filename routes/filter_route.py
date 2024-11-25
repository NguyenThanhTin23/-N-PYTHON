from flask import Blueprint, request, redirect, render_template
from routes.paginate import paginate_data
import pandas as pd
from FEATURE.filter_data import filter_dataframe

file_path = 'data_dirty.csv' 
filtered_file_path = 'FEATURE/filtered_data.csv'

data = pd.read_csv(file_path) 
ROWS_PER_PAGE = 12
filter_bp = Blueprint('filter', __name__, url_prefix='/filter')
@filter_bp.route('/filter', methods=['GET', 'POST'])
def filter_data():
    if request.method == 'POST':  # Khi nhấn nút lọc dữ liệu
        # Lấy các giá trị từ form
        date_start = request.form.get('DateStart', '')
        date_end = request.form.get('DateEnd', '')
        country = request.form.get('Country', '')
        region = request.form.get('Region', '')
        # Đọc dữ liệu từ file gốc
        data = pd.read_csv(file_path)
        # Thực hiện lọc dữ liệu dựa trên các giá trị đã nhập
        filtered_data = filter_dataframe(
            data,
            date_start=date_start,
            date_end=date_end,
            country=country,
            region=region
        )

        # Lưu dữ liệu đã lọc vào file CSV (tạm thời hoặc để tải về sau)
        filtered_data['Date'] = filtered_data['Date'].dt.strftime('%d/%m/%Y')
        filtered_data.to_csv(filtered_file_path, index=False)


        # Chuyển hướng đến trang phân trang để xem dữ liệu đã lọc
        return redirect('/filter/filter?page=1')

    # Lấy số trang hiện tại từ query params (nếu không có thì mặc định là 1)
    page = int(request.args.get('page', 1))

    # Nếu không có dữ liệu đã lọc, đọc dữ liệu từ file gốc
    filtered_data = pd.read_csv(filtered_file_path)

    # Phân trang dữ liệu
    pagination = paginate_data(filtered_data, page, ROWS_PER_PAGE)

    # Hiển thị dữ liệu trên giao diện
    return render_template(
        'filter.html',
        table_data=pagination["table_data"],
        headers=filtered_data.columns,
        page=page,
        total_pages=pagination["total_pages"],
        has_next=pagination["has_next"],
        has_prev=pagination["has_prev"],
        nearby_pages=pagination["nearby_pages"],
    )