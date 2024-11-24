import pandas as pd
import os
def isExist(file_path):
    """
    Kiểm tra file có tồn tại không ?
    file_path : đường dẫn tới file đầu vào

    """
    if not os.path.exists( file_path ):
        print(f"File không tồn tại !")
        return False
    return True

def load_csv(file_path):
    """
    Đọc file csv 
    file_path : đường dẫn tới file đầu vào

    """

    if not isExist( file_path):
        return None
    return pd.read_csv( file_path )

def save_csv( data, output_file):
    """
    Lưu dữ liệu vào file csv đầu ra
    output_file : đường dẫn tới file đầu ra
    data : dữ liệu DataFrame

    """

    data.to_csv( output_file, index = False) 
    print(f"Dữ liệu đã được lưu vào : {output_file}")

def filter_simple(data):
    """
    Lọc dữ liệu một cột theo giá trị cụ thể
    data : dữ liệu DataFrame

    """
    print("\nDanh sách các cột trong dữ liệu : ")
    #Hiển thị danh sách các cột
    print( data.columns.tolist() )  

    column_name = input("Nhập tên cột để lọc : ").strip()
    while column_name not in data.columns : 
        print(f"Cột ' {column_name} ' không tồn tại ! Vui lòng thử lại.")
        column_name = input("Nhập tên cột để lọc : ").strip()

    #Chuyển đổi 'Date' sang kiểu datetime
    if column_name == 'Date':
        data['Date'] = pd.to_datetime( data['Date'] , errors = 'coerce')
        value = input(f"Nhập thời gian cần lọc (theo định dạng : YYYY-MM-DD) ").strip()
        try:
            filtered_data = data[ data['Date'] == pd.to_datetime(value) ]
        except Exception :
            print (f"Lỗi khi lọc ngày : {Exception}")
            return pd.DataFrame()
    #Trường hợp lọc cột 'Country/Region' và 'WHO Region' ( cột chứa giá trị chữ )
    elif column_name == 'Country/Region':
        value = input(f"Nhập quốc gia cần lọc : ").strip()
        filtered_data = data[ data['Country/Region'].str.contains(value, case = False, na = False)]
    elif column_name == 'WHO Region':
        value = input(f"Nhập giá trị cần lọc trong cột ' {column_name} ': ").strip()
        filtered_data = data[ data['WHO Region'].str.contains(value, case = False, na = False)]
    #Các trường hợp lọc các cột còn lại ( cột chứa các giá trị số )
    else:
        try:
            filtered_data = data[ data[column_name] == value ]
        except Exception :
            print(f"Lỗi khi lọc dữ liệu : ")
            return pd.DataFrame()

    return filtered_data 


def filter_advanced(data):
    """
    Lọc dữ liệu nâng cao : với nhiều điều kiện theo toán tử, với nhiều cột
    data : dữ liệu DataFrame
    
    """
    print("\nDanh sách các cột trong dữ liệu : ")
    #Hiển thị danh sách các cột
    print( data.columns.tolist() )

    while True:
        try:
            num_conditions = int( input("Nhập số lượng điều kiện lọc : ").strip() )
            if num_conditions <= 0:
                raise ValueError("Số lượng điều kiện phải lớn hơn 0.")
            break
        except ValueError :
            print(f"Lỗi {ValueError}. Vui lòng nhập lại.")


    conditions = []    #Danh sách các điều kiện
    
    for i in range( num_conditions ):
        print(f"\nNhập điều kiện {i+1}: ")
        column_name = input("Nhập tên cột : ").strip()
        while column_name not in data.columns : 
            print(f"Cột ' {column_name} ' không tồn tại ! vui lòng nhập lại.")
            column_name = input("Nhập tên cột : ").strip()

        #Chuyển đổi 'Date' sang kiểu datetime và chọn điều kiện
        if column_name == 'Date':
            data['Date'] = pd.to_datetime( data['Date'], errors = 'coerce')
            print("1. Ngày cụ thể")
            print("2. Từ một ngày trở đi")
            print("3. Từ một ngày trở lại")

            choice = input("Chọn kiểu điều kiện : ").strip()
            value = input(f"Nhập thời gian theo định dạng (YYYY-MM-DD) : ").strip()

            if choice == '1':
                conditions.append( data['Date'] == pd.to_datetime(value) )
            elif choice == '2':
                conditions.append( data['Date'] >= pd.to_datetime(value) )
            elif choice == '3':
                conditions.append( data['Date'] <= pd.to_datetime(value) )
            else:
                print("Toán tử không hợp lệ.")
                return pd.DataFrame()
            
        #Trường hợp lọc cột 'Country/Region' và 'WHO Region' ( cột chứa giá trị chữ )
        elif column_name == 'Country/Region':
            value = input(f"Nhập quốc gia cần lọc : ").strip()
            conditions.append( data['Country/Region'].str.contains(value, case = False, na = False ))
        elif column_name == 'WHO Region':
            value = input(f"Nhập khu vực cần lọc : ").strip()
            conditions.append( data['WHO Region'].str.contains(value, case = False, na = False ))

        #Các trường hợp lọc các cột còn lại ( cột chứa các giá trị số ) và chọn điều kiện
        else:
            print("1. Bằng ")
            print("2. Lớn hơn ")
            print("3. Nhỏ hơn ")
            print("4. Lớn hơn hoặc bằng ")
            print("5. Nhỏ hơn hoặc bằng ")
            print("6. Khác ")

            choice = input("Chọn điều kiện : ").strip()
            value = input(f"Nhập giá trị cho cột ' {column_name} ' : ").strip()

            if choice == '1':
                conditions.append( data[column_name] == value )
            elif choice == '2':
                conditions.append( data[column_name] > float(value) )
            elif choice == '3':
                conditions.append( data[column_name] < float(value) )
            elif choice == '4':
                conditions.append( data[column_name] >= float(value) )
            elif choice == '5':
                conditions.append( data[column_name] <= float(value) )
            elif choice == '6':
                conditions.append( data[column_name]  != value )
            else:
                print("Toán tử không hợp lệ.")
                return pd.DataFrame()

    #Nếu chỉ có một điều kiện thì lọc trực tiếp điều kiện đó
    if num_conditions == 1:
       filtered_data = data.loc[ conditions[0] ]
    #Nếu có nhiều điều kiện thì lọc kết hợp theo yêu cầu người dùng
    else:
        print("\n Bạn muốn kết hợp các điều kiện thế nào ? ")
        print("1. Thoả mãn tất cả điều kiện ")   
        print("2. Thoả mãn ít nhất một điều kiện ")

        choice = input("Lựa chọn : ").strip()

        if choice == '1':
            combined_condition = conditions[0]
            for cond in conditions[ 1: ]:
                combined_condition &= cond
        elif choice == '2':
            combined_condition = conditions[0]
            for cond in conditions[ 1: ]:
                combined_condition |= cond
        filtered_data = data.loc[ combined_condition ]

    return filtered_data

"""
if __name__ =="__main__":
    print("Lọc dữ liệu\n")
    file_path = input("Nhập đường dẫn tới file csv đầu vào : ").strip()
    output_file = input("Nhập đường dẫn tới file csv đầu ra : ").strip()

    data = load_csv(file_path)
    if data is None:
        exit()

    while True:
        print("\nChọn loại filter : ")
        print("1. Lọc theo một cột với giá trị cụ thể")
        print("2. Lọc theo nhiều điều kiện")

        filter_choice = input("Lựa chọn : ").strip()

        if filter_choice == '1':
            filtered_data = filter_simple(data)
        elif filter_choice == '2':
            filtered_data = filter_advanced(data)
        else:
            print("Lựa chọn không hợp lệ !")
            continue

        if not filtered_data.empty :
            save_csv( filtered_data, output_file)
        else:
            print("Không có dữ liệu sau khi lọc !")

        another = input("Bạn có muón thực hiện lọc nữa không ? (Y/N)").strip()

        if another != 'y':
            break
"""