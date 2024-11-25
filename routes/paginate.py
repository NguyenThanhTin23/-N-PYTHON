def paginate_data(data, page, rows_per_page):  
    start_idx = (page - 1) * rows_per_page  
    end_idx = start_idx + rows_per_page  
    paginated_data = data.iloc[start_idx:end_idx]  
    table_data = paginated_data.to_dict(orient='records')  
    total_pages = (len(data) + rows_per_page - 1) // rows_per_page  
    start_page = max(1, page - 2)  
    end_page = min(total_pages, page + 2)  
    nearby_pages = range(start_page, end_page + 1)  

    return {  
        "table_data": table_data,  
        "total_pages": total_pages,  
        "has_next": page < total_pages,  
        "has_prev": page > 1,  
        "nearby_pages": nearby_pages,  
    }