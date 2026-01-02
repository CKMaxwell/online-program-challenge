# 20200816 - Luke, I Am Your ...
def relation_to_luke(name):
    name_dic = {"Darth Vader": "father", "Leia": "sister", "Han": "brother in law", "R2D2": "droid"}
    ans = "Luke, I am your {}.".format(name_dic[name])
    return ans


result = relation_to_luke("Darth Vader")
print(result)