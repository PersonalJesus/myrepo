arr_count = 0
with open('input01.txt', 'r') as data_input:
    for i in data_input:
        if int(i) == 1:
            arr_count += 1
            print(arr_count)
#            print(i)