
#reverse the string without slicing

sting = "imastring"
rev = ""
for char in sting:
    rev = char + rev
print(rev)


#Palindrome 
def Palindrome(val):
    st , en = 0, len(val)-1
    while st < en:
        if val[st] != val[en]:
            return False
        st +=1
        en -=1
    return True

val = "icananaaci"
isPal = Palindrome(val)
if isPal:
    print(f"{val}is a Palindrome")
else:
    print("not a Palindrome")
    
######.   Count vowels     $$$$$$$

val = "jgajshaoacis"
vowel = 0
vowelletters = 'aeiouAEIOU'
for char in val:
    if char in vowelletters:
        vowel+=1
print(vowel)

#### Character frequency (manual) ##


def frequec(val):
    freq = {}
    for item in val:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
    
val = "im ins asnggood"
print(frequec(val))


# Sort the characters of the string
my_string = "hello"

# Sort the characters of the string
sorted_characters = sorted(my_string)
print(f"Sorted characters (list): {sorted_characters}")

# Join the sorted characters back into a string
sorted_string = "".join(sorted_characters)
print(f"Sorted string: {sorted_string}")

# Example with a different string
another_string = "python"
sorted_another_string = "".join(sorted(another_string))
print(f"Sorted 'python': {sorted_another_string}")














            