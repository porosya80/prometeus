def counter(a, b):
    a = set(str(a))
    b = set(str(b))
    result = 0

    for i in a:
        if i in b:
            result += 1
    return result








print(counter(12345, 567))