from flask import Blueprint, send_file
import os

# Tạo một Blueprint cho các route download
downloads_bp = Blueprint('downloads', __name__)

# Đường dẫn tệp cần tải xuống
cleaned_file_path = 'FEATURE/cleaned_data.csv' 
filtered_file_path = 'FEATURE/filtered_data.csv' 
stats_file_path = 'STATISTICAL/statistics_data.csv'
sort_file_path = 'FEATURE/sort.csv'
chart_path = 'static/chart.png'

@downloads_bp.route('/download_clean_data')
def download_clean_data():
    return send_file(cleaned_file_path, as_attachment=True)

@downloads_bp.route('/download_filtered_data')
def download_filtered_data():
    return send_file(filtered_file_path, as_attachment=True)

@downloads_bp.route('/download_statistics_data')
def download_statistics_data():
    return send_file(stats_file_path, as_attachment=True)

@downloads_bp.route('/download_sort_data')
def download_sort_data():
    return send_file(sort_file_path, as_attachment=True)

@downloads_bp.route('/download_chart')
def download_chart():
    return send_file(chart_path, as_attachment=True)
