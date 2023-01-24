def count_sheep(n):
    a = []
    if n == 0:
        return ""
    else:
        for i in range(1, n):
            a = a.append(str(i) + "sheep...")
    return a
    
print(count_sheep (5))