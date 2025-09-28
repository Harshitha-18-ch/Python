string=input("enter the String:").lower()
vowel,consonant=0,0
for ch in string:
    if ch.isalpha():
        if ch in "aeiou":
            vowel+=1
        else:
            consonant+=1
print(f"Vowel Cout is {vowel}")
print(f"Consonant Count is {consonant}")