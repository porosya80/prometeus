def clean_list(list_to_clean):
    list_str = [str(i) for i in list_to_clean]
    list_str = set(list_str)
    result_list = [int(i) for i in list_str]
    return result_list






print (clean_list([32, 32.1, 32.0, -123]))