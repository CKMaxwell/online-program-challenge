# 20201002 - Percentage Changed
def percentage_changed(old, new):
    old2 = float(old[1:])
    new2 = float(new[1:])
    percentage = str(round(abs((1 - (new2 / old2))*100)))
    if old2 > new2:
        return percentage + "% decrease"
    elif old2 < new2:
        return percentage + "% increase"

print(percentage_changed("$800", "$600"))