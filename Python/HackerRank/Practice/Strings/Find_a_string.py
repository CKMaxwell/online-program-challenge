# 20200625 - Find a string
def count_substring(string, sub_string):
    count_df = 0
    ran =  len(string) - len(sub_string) + 1
    for i in range(0,ran):
        if string[i:i+len(sub_string)] == sub_string:
            count_df = count_df + 1
    return count_df


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)