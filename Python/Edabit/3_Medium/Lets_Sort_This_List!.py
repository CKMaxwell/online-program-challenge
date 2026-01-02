# 20200928 - Let's Sort This List!
def asc_des_none(lst, s):
    if s == "Asc":
        lst.sort()
        return lst
    elif s == "Des":
        lst.sort(reverse = True)
        return lst
    elif s == "None":
        return lst


print(asc_des_none([4, 3, 2, 1], "Asc" ))