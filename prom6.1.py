def count_holes(n):

        check_list = [str(_) for _ in range(10)]
        check_list.append("-")
        print(check_list)
        check_result = True
        for chr in str(n):
            if chr not in check_list:
                check_result = False
                break
        if len(str(n)) == 0:
            check_result = False


        if not check_result:
            return "ERROR"
        n = str(n).replace("-" , "")
        if len(str(n)) != 1:
            n = str(n).lstrip("0")

        result = 0

        holes = {1: 0,
                 2: 0,
                 3: 0,
                 4: 1,
                 5: 0,
                 6: 1,
                 7: 0,
                 8: 2,
                 9: 1,
                 0: 1}

        for ch in str(n):
            result += holes[int(ch)]

        return result


print(count_holes(''))


