def process_raw_data (input_string):
    input_string = input_string.replace (' ', '')
    s = input_string.split(',')
    res = dict()
    for i in s:
        res[i.split('=')[0]] = i.split ('=')[1]
    return res
print (process_raw_data ('name  = Иван, age  = 25, city =  Москва'))
