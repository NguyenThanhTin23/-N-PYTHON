import pandas as pd

def delete_empty(df):
    """
    Xoá các hàng và cột trống khỏi DataFrame, sau đó thay thế giá trị còn thiếu bằng 0.
    
    Parameters:
    df (pd.DataFrame): DataFrame cần xử lý.
    
    Returns:
    pd.DataFrame: DataFrame sau khi xoá hàng/cột trống và thay giá trị thiếu bằng 0.
    """
    df = df.dropna(how='all')  # Xoá các hàng chỉ chứa giá trị NA
    df = df.dropna(axis=1, how='all')  # Xoá các cột chỉ chứa giá trị NA
    df = df.fillna(0)  # Điền các giá trị NA còn lại bằng 0
    return df

def format_number(df):
    """
    Chuyển tất cả các cột có kiểu số (float, int) trong DataFrame sang kiểu số nguyên (int).
    
    Parameters:
    df (pd.DataFrame): DataFrame cần xử lý.
    
    Returns:
    pd.DataFrame: DataFrame sau khi chuyển đổi các cột số sang kiểu số nguyên.
    """
    numeric_columns = df.select_dtypes(include=['float', 'int']).columns
    for col in numeric_columns:
        df[col] = df[col].astype(int)
    return df

def cleanData(file_path):
    """
    Làm sạch dữ liệu từ file CSV với các thao tác sau:
    1. Xoá hàng/cột trống và thay giá trị thiếu bằng 0.
    2. Chuyển tất cả các cột số sang kiểu số nguyên.
    3. Thay giá trị âm bằng giá trị tuyệt đối.
    4. Xoá ký tự đặc biệt khỏi các cột (trừ cột 'Date').
    5. Chuyển các cột 'Country/Region' và 'WHO Region' thành chữ dạng title.
    6. Chuyển cột 'Date' về định dạng DD/MM/YYYY.
    7. Xoá các hàng trùng lặp và giữ lại hàng đầu tiên.

    Parameters:
    file_path (str): Đường dẫn tới file CSV cần làm sạch.

    Returns:
    pd.DataFrame: DataFrame sau khi làm sạch dữ liệu.
    """
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(file_path)

    # Xoá giá trị NA
    df = delete_empty(df)

    # Chuyển toàn bộ dữ liệu dạng số thành số nguyên
    df = format_number(df)

    # Thay giá trị nhỏ hơn 0 bằng trị tuyệt đối
    numeric_columns = df.select_dtypes(include=['int', 'float']).columns
    for col in numeric_columns:
        df[col] = df[col].abs()

    # Xoá kí tự đặc biệt
    for column in df.columns: 
        if column != 'Date': 
            df[column] = df[column].astype(str).str.replace(r"[^\w\s]", "", regex=True)

    # Chuyển dữ liệu cột 'Country/Region' và 'WHO Region' thành dạng title
    df['Country/Region'] = df['Country/Region'].str.title()
    df['WHO Region'] = df['WHO Region'].str.title()

    # Đổi định dạng ngày thành DD/MM/YYYY
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True, errors='coerce')
    df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')

    # Xoá các hàng trùng lặp và giữ lại hàng đầu tiên
    df = df.drop_duplicates(keep='first')

    return df
