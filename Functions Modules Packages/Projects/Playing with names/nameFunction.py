def ispalindrome(name):
    if name == name[::-1]:
        return "Yes it is palindrome"
    else:
        return "It is not palindrome"

def count_the_vowels(name):
    count=0
    vowels="aeiouAEIOU"
    for ch in name:
        if ch in vowels:
            count += 1
    return count

def frequency_of_letters(name):
    frequency ={}
    for ch in name:
        if ch == " ":
            continue
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch]=1
    return frequency