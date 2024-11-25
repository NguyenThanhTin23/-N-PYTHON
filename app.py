from flask import Flask
from routes.crud_route import crud_bp
from routes.index_route import index_bp
from routes.clean_route import clean_bp
from routes.statistics_route import statistics_bp
from routes.filter_route import filter_bp
from routes.sort_route import sort_bp
from routes.chart_route import chart_bp
from routes.downloads import downloads_bp
app = Flask(__name__, static_folder='static')  
app.secret_key = 'your_secret_key_here'  

app.register_blueprint(index_bp)
app.register_blueprint(crud_bp)
app.register_blueprint(clean_bp)
app.register_blueprint(statistics_bp)
app.register_blueprint(filter_bp)
app.register_blueprint(sort_bp)
app.register_blueprint(chart_bp)
app.register_blueprint(downloads_bp, url_prefix='/download')

if __name__ == '__main__':
    app.run(debug=True)