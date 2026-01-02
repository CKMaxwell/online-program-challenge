# 20200921 - Incorrect Import Statement
def fix_import(s):
    word = s.split()
    correct = word[2] + " " + word[3] + " " + word[0] + " " + word[1]
    return correct

print(fix_import("import object from module_name"))