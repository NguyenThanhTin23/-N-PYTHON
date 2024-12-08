from flask import Blueprint, request, redirect, flash, render_template
from routes.paginate import paginate_data
from CRUD.Creat import creat
from CRUD.Update import update  
from CRUD.Delete import delete
import pandas as pd
import os
crud_bp = Blueprint('crud', __name__, url_prefix='/crud')
file_path = 'data_dirty.csv'  
data = pd.read_csv(file_path) 
ROWS_PER_PAGE = 12
@crud_bp.route('/add', methods=['GET', 'POST']) 
def add_data():  
    if request.method == 'POST': 
        Country_Region = request.form['Country_Region'] 
        Date = request.form['Date']    
        Confirmed = int(request.form['Confirmed'])  
        Deaths = int(request.form['Deaths'])  
        Recovered = int(request.form['Recovered'])  
        Active = int(request.form['Active'])  
        New_cases = int(request.form['New_cases'])  
        New_deaths = int(request.form['New_deaths'])  
        New_recovered = int(request.form['New_recovered'])  
        WHO_Region = request.form['WHO_Region']  
        new_row = [Date, Country_Region, Confirmed, Deaths, Recovered, Active, New_cases, New_deaths, New_recovered, WHO_Region]  

        try:  
            creat(file_path, new_row)  
            flash("Dòng mới đã được thêm vào thành công!", 'success')  
            return redirect('/crud/add')  
        except Exception as e:  
            flash(f"Lỗi: {str(e)}", 'danger')  
            return redirect('/crud/add')  
    return render_template('add.html')  

# Thêm route xử lý tải lên file CSV  
@crud_bp.route('/upload_csv', methods=['GET', 'POST'])
def upload_csv():  
    if 'file' not in request.files:  
        flash('Không có tệp nào được chọn', 'danger')  
        return redirect('/crud/add')  

    file = request.files['file']  
    if file.filename == '':  
        flash('Tệp không hợp lệ', 'danger')  
        return redirect('/crud/add')  

    if file and file.filename.endswith('.csv'):  
        try:  
            file_upload = os.path.join('uploads', file.filename)  
            file.save(file_upload)  

            # Đọc tệp CSV và kiểm tra các trường dữ liệu  
            new_data = pd.read_csv(file_upload)  
            if set(new_data.columns) != set(data.columns):  
                flash('Tệp CSV không có cùng các trường dữ liệu với dữ liệu hiện có', 'danger')  
                return redirect('/crud/add')  

            # Thêm dữ liệu mới vào dữ liệu hiện có  
            new_data.to_csv(file_path, mode='a', header=False, index=False)  
            flash(f'Dữ liệu từ {file.filename} đã được thêm thành công!', 'success')  
            return redirect('/crud/add')  
        except Exception as e:  
            flash(f"Lỗi khi thêm dữ liệu từ tệp CSV: {str(e)}", 'danger')  
            return redirect('/crud/add')  

    flash('Vui lòng chọn tệp CSV hợp lệ', 'danger')  
    return redirect('/crud/add') 
# Các route khác cho chức năng sửa, xóa, làm sạch, thống kê và biểu đồ  
@crud_bp.route('/update', methods=['GET', 'POST'])
def update_data():
    if request.method == 'POST':  
        date_to_search = request.form.get('Date')  
        country_to_search = request.form.get('Country_Region')  

        if 'Confirmed' in request.form:  # Nếu tồn tại trường Confirmed, nghĩa là đang cập nhật dữ liệu  
            try:  
                # Validate dữ liệu đầu vào  
                updated_data = [  
                    request.form['Date'],  
                    request.form['Country_Region'],  
                    int(request.form['Confirmed']),  
                    int(request.form['Deaths']),  
                    int(request.form['Recovered']),  
                    int(request.form['Active']),  
                    int(request.form['New_cases']),  
                    int(request.form['New_deaths']),  
                    int(request.form['New_recovered']),  
                    request.form['WHO_Region']  
                ]  
                
                # Thực hiện update  
                update(file_path, updated_data)  
                
                # Flash message chi tiết bằng tiếng Việt   
                flash(f"Cập nhật dữ liệu cho {updated_data[1]} vào ngày {updated_data[0]} thành công!", 'success')  
            except ValueError as ve:  
                # Bắt lỗi nhập số không hợp lệ  
                flash(f"Đầu vào không hợp lệ: {str(ve)}. Vui lòng nhập các giá trị số chính xác.", 'danger')  
            except Exception as e:  
                # Bắt các lỗi khác  
                flash(f"Lỗi khi cập nhật bản ghi: {str(e)}", 'danger')  
            
            return redirect('/crud/update')  
        
        # Nếu chỉ tìm kiếm  
        try:  
            data = pd.read_csv(file_path)  
            
            # Xử lý ngày tháng chính xác hơn  
            data['Date'] = pd.to_datetime(data['Date'], format='mixed', dayfirst=True, errors='coerce')  
            data['Date'] = data['Date'].dt.strftime('%d/%m/%Y')  

            # Tìm kiếm không phân biệt hoa thường  
            record = data[  
                (data['Date'] == date_to_search) &   
                (data['Country/Region'].str.lower() == country_to_search.lower())  
            ]  
            
            if not record.empty:  
                # Convert record to a dictionary for easier access in the template  
                record_dict = record.iloc[0].to_dict()  
                return render_template('update.html', record=record_dict)  
            else:  
                # Nếu không tìm thấy bản ghi  
                flash(f"Không tìm thấy bản ghi cho {country_to_search} vào ngày {date_to_search}", 'warning')  
                return render_template('update.html', search=True)  
        
        except Exception as e:  
            # Xử lý các lỗi có thể xảy ra khi đọc file  
            flash(f"Lỗi khi tìm kiếm bản ghi: {str(e)}", 'danger')  
            return render_template('update.html')  

    # Nếu không có yêu cầu POST, chỉ hiển thị trang update  
    return render_template('update.html')

@crud_bp.route('/delete', methods=['GET', 'POST'])
def delete_data():
    data = pd.read_csv(file_path)
    page = int(request.args.get('page', 1))
    pagination = paginate_data(data, page, ROWS_PER_PAGE)

    # Xử lý xóa dữ liệu khi người dùng gửi form
    if request.method == 'POST':
        rows_to_delete = request.form.getlist('rows_to_delete')
        if rows_to_delete:
            rows_to_delete = [int(row)+(page-1)*12 for row in rows_to_delete]
            # Xóa các dòng được chọn
            delete(file_path,data,rows_to_delete)
            flash("Dữ liệu đã được xóa thành công!", 'success')
            return redirect('/crud/delete')

    return render_template(
        'delete.html',
        table_data=pagination["table_data"],
        page=page,
        total_pages=pagination["total_pages"],
        has_next=pagination["has_next"],
        has_prev=pagination["has_prev"],
        nearby_pages=pagination["nearby_pages"]
    )
