
def clean_list(list_to_clean):
    result=[]

    for i in range(len(list_to_clean)):
        list=list_to_clean[:i]
        print(list)
        for n in range(len(list)):
            # n=n+1
            if list_to_clean[i]== list[n] and type(list[n])==type(list_to_clean[i]) :
                list_to_clean[i]=""
        result.append(list_to_clean[i])
    for i in result:
        if i=="":
            while result.count("")>0:
                result.remove(i)
    return result





result = clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5])
print(result)