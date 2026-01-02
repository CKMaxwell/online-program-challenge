#20200923 - The Karaca's Encryption Algorithm
def encrypt(word):
    tran_dic = {"a": 0, "e": 1, "i": 2, "o": 2, "u": 3}
    new = ""
    for i in range(len(word)-1, 0-1, -1):
        if word[i] in tran_dic:
            new = new + str(tran_dic[word[i]])
        else:
            new = new + word[i]
    return new + "aca"


print(encrypt("banana"))