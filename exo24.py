def nmbr_char(str):
    char_counter = {}
    for char in str:
        if char in char_counter:
            char_counter[char] +=1
        else:
            char_counter[char]=1
    return char_counter


def anagrams(str1 :str,str2:str):
    if len(str1)!=len(str2):
        return False
    char_counter1=nmbr_char(str1)
    char_counter2=nmbr_char(str2)
    for char in str1:
        if char not in str2:
            return False
        # char in str1 and str2 -> no error 
        if char_counter1[char] != char_counter2[char]:
            return False
    return True


print(anagrams("abc","der"))
print(anagrams("tan","nta"))
print(anagrams("nnnaatt","tatnnan"))





