from flask import Blueprint, request, redirect, flash, render_template
from routes.paginate import paginate_data
from FEATURE.clean import cleanData
import pandas as pd



file_path = 'data_dirty.csv' 
cleaned_file_path = 'FEATURE/cleaned_data.csv'  
data = pd.read_csv(file_path) 
ROWS_PER_PAGE = 12

clean_bp = Blueprint('clean', __name__, url_prefix='/clean')
@clean_bp.route('/clean', methods=['GET', 'POST'])
def clean_data():
    if request.method == 'POST':  # Chỉ thực hiện khi nhấn nút "Clean"
        # Làm sạch dữ liệu
        cleaned_data = cleanData(file_path)

        # Lưu dữ liệu đã làm sạch vào file CSV
        cleaned_data.to_csv(cleaned_file_path, index=False)
        cleaned_data.to_csv(file_path, index=False)

        flash("Dữ liệu đã được làm sạch thành công!", "success")

        # Chuyển hướng để hiển thị dữ liệu đã làm sạch
        return redirect('/clean/clean')

    # Phân trang dữ liệu hiện tại (chưa làm sạch nếu chưa nhấn nút)
    data = pd.read_csv(file_path)
    page = int(request.args.get('page', 1))
    pagination = paginate_data(data, page, ROWS_PER_PAGE)

    # Hiển thị dữ liệu trên giao diện
    return render_template(
        'clean.html',
        table_data=pagination["table_data"],
        headers=data.columns,
        page=page,
        total_pages=pagination["total_pages"],
        has_next=pagination["has_next"],
        has_prev=pagination["has_prev"],
        nearby_pages=pagination["nearby_pages"],
    )