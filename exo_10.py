def isPalindrome(word):
    half_word=len(word)//2
    i=0
    while(i<=half_word):
        if word[i] != word[len(word)-1-i]:
            return False
        i+=1
    return True    


word=str(input("entrer un mot: "))
if isPalindrome(word):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
















#word=str(input("please enter a word : "))

