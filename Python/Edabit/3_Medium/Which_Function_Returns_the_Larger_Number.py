# 20201020 - Which Function Returns the Larger Number?
# 此題參考資料有lambda的解說
def which_is_larger(f, g):
    if f() > g():
        return "f"
    elif f() < g():
        return "g"
    elif f() == g():
        return "neither"

print(which_is_larger(lambda: 25,  lambda: 25))
