from flask import Blueprint, request, render_template
import shutil

chart_bp = Blueprint('chart', __name__, url_prefix='/chart')
@chart_bp.route('/chart', methods=['GET', 'POST'])
def chart():
    chart_url = None
    if request.method == 'POST':
        chart_type = request.form['chart_type']
        
        # Vẽ biểu đồ dựa trên loại người dùng chọn
        if chart_type == 'cases_by_region':
            chart_url = 'static/chart_region.png'
        elif chart_type == 'new_cases_month':
            chart_url = 'static/monthly_chart.png'
        elif chart_type == 'cases_by_world':
            chart_url = 'static/monthly_new_chart.png'
        elif chart_type == 'cases_region_monthly':
            chart_url = 'static/region_monthly_chart.png'

        shutil.copy(chart_url, 'static/chart.png')
    return render_template('chart.html', chart_url=chart_url)