def clean_list(list_to_clean):
    for ind in (range(len(list_to_clean)-1)):
        for key in (range(ind+1, len(list_to_clean))):
            if list_to_clean[ind] == list_to_clean[key] and type(list_to_clean[ind]) == type(list_to_clean[key]):
                list_to_clean[key] = "X"
    while list_to_clean.count("X") != 0:
        list_to_clean.remove("X")

    return list_to_clean





print(clean_list(['qwe', 'reg', 'qwe', 'REG']))
# clean_list(['qwe', 'reg', 'qwe', 'REG'])