# 20201029 - Building a Pie Chart
def pie_chart(data):
    total = 0
    for i in data:
        total += data[i]
    # 以上這段可以簡寫為  total = sum(data.values())  或 total = sum(v for k,v in data.items())

    for j in data:
        data[j] = round((360/total) * data[j], 1)
    return data

print(pie_chart({ "a": 30, "b": 15, "c": 5}))