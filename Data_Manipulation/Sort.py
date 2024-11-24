import pandas as pd
import os

def isExist(file_path):
    """
    Kiểm tra file có tồn tại không 
    file_path : đường dẫn đến file csv đầu vào
    """
    if not os.path.exists( file_path ):
        print(f"Không tồn tại : {file_path}")
        return False
    else:
        return True



def sort_date_country(file_path, output_file, ascending):
    """
    Hàm sắp xếp dữ liệu theo 'Country/Region'
    file_path : đường dẫn đến file csv đầu vào
    ascending : thứ tự sắp xếp, True là tăng dần, False là giảm dần
    output_file :  đường dẫn đến file csv đầu ra
    """
    # Kiểm tra file_path có tồn tại không
    if not isExist(file_path):
        return

    # Đọc dữ liệu từ file csv
    data = pd.read_csv( file_path )

    #Chuẩn hoá tên cột 
    data.columns = data.columns.str.strip()

    #Chuyển đổi 'Date' sang kiểu datetime
    data['Date'] = pd.to_datetime( data['Date'], errors = 'coerce')

    sorted_data = data.sort_values( by = ['Date', 'Country/Region'], ascending = ascending)

    #Lưu dữ liệu đã sắp xếp
    sorted_data.to_csv( output_file, index = False)
    print(f"\n Dữ liệu đã được lưu vào {output_file}")




def sort_column(file_path, output_file, ascending, column_name):
    """
    Hàm sắp xếp dữ liệu theo một cột 
    file_path : đường dẫn đến file csv đầu vào
    output_file :  đường dẫn đến file csv đầu ra
    ascending : thứ tự sắp xếp, True là tăng dần, False là giảm dần
    column_name : tên cột cần sắp xếp
    """
    # Kiểm tra file_path có tồn tại không
    if not isExist(file_path):
        return
    
    # Đọc dữ liệu từ file csv
    data = pd.read_csv( file_path )

    #Chuẩn hoá tên cột 
    data.columns = data.columns.str.strip()

    #Nếu là 'Date' thì cần chuyển đổi sang datetime
    if column_name == 'Date':
        data['Date'] = pd.to_datetime( data['Date'], errors = 'coerce')
        if data['Date'].isnull().all():
            print("Có dữ liệu không hợp lệ ở {column_name}")
            return
    
    #Kiểm tra dữ liệu của cột có còn không
    if column_name not in data.columns:
        print(f"{column_name} không tồn tại! Vui lòng kiểm tra !")
        return

    #Sắp xếp dữ liệu 
    sorted_data = data.sort_values( by = [column_name], ascending = ascending)

    #Lưu dữ liệu đã sắp xếp vào file đ
    sorted_data.to_csv( output_file, index = False)
    print(f"\n Dữ liệu đã được lưu vào {output_file}")
    

"""
if __name__=="__main__":
    file_path = input("Nhập đường dẫn tới file csv : ").strip()
    output_file = input("Nhập đường dẫn file đầu ra : ").strip()

    print("Menu sắp xếp : ")
    print("1. Sắp xếp theo Date và Country/Region")
    print("2. Sắp xếp theo Confirmed")
    print("3. Sắp xếp theo Deaths")
    print("4. Sắp xếp theo Recovered")
    print("5. Sắp xếp theo Active")
    print("6. Sắp xếp theo New cases")
    print("7. Sắp xếp theo New deaths")
    print("8. Sắp xếp theo New recovered")
    print("9. Sắp xếp theo WHO Region")

    choice = input("Nhập lựa chọn : ").strip()

    order = input("Sắp xếp tăng dần (True) hoặc giảm dần (False) : ").strip().lower()
    ascending = True if order in ['true', 't', '1', ''] else False
    
    if choice == '1':
        sort_date_country(file_path, output_file, ascending)
    elif choice == '2':
        sort_column(file_path, output_file, ascending, "Confirmed")
    elif choice == '3':
        sort_column(file_path, output_file, ascending, "Deaths")
    elif choice == '4':
        sort_column(file_path, output_file, ascending, "Recovered")
    elif choice == '5':
        sort_column(file_path, output_file, ascending, "Active")
    elif choice == '6':
        sort_column(file_path, output_file, ascending, "New cases")
    elif choice == '7':
        sort_column(file_path, output_file, ascending, "New deaths")
    elif choice == '8':
        sort_column(file_path, output_file, ascending, "New recovered")
    elif choice == '9':
        sort_column(file_path, output_file, ascending, "WHO Region")
    else:
        print("Lựa chọn không hợp lệ!")
"""