entry_data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_func(data):
    res_list = []
    try:
        [res_list.append(sum(list(map(int, i.split(","))))) for i in data]
    except ValueError:
        res_list.append("Не можу це зробити")
    print(res_list)
sum_func(entry_data)