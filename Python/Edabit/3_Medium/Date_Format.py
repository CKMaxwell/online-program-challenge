# 20200917 - Date Format
def format_date(date):
    return date[6:9+1] + date[3:4+1] + date[0:1+1]

print(format_date("11/12/2019"))