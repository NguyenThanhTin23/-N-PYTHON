from flask import Blueprint, request, render_template
import pandas as pd
from routes.paginate import paginate_data

file_path = 'data_dirty.csv'  
data = pd.read_csv(file_path) 
ROWS_PER_PAGE = 12

index_bp = Blueprint('index', __name__, url_prefix='/')
@index_bp.route('/', methods=['GET', 'POST']) 
def index():  
    # Đọc lại dữ liệu từ tệp CSV để đảm bảo có dữ liệu mới  
    data = pd.read_csv(file_path)  
    page = int(request.args.get('page', 1))  
    pagination = paginate_data(data, page, ROWS_PER_PAGE)  
    
    return render_template(  
        'index.html',  
        table_data=pagination["table_data"],  
        headers=data.columns,  
        page=page,  
        total_pages=pagination["total_pages"],  
        has_next=pagination["has_next"],  
        has_prev=pagination["has_prev"],  
        nearby_pages=pagination["nearby_pages"]  
    )  