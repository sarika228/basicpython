def areAnagram(str1, str2):
    # Get lengths of both strings
    n1 = len(str1)
    n2 = len(str2)
 
    # If length of both strings is not same, then
    # they cannot be anagram
    if n1 != n2:
        return 0
 
    # Sort both strings
    str1 = sorted(str1)
    str2 = sorted(str2)
 
    # Compare sorted strings
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return 0
 
    return 1
    # Driver code
str1 = "dog"
str2 = "god"
 
# Function Call
if areAnagram(str1, str2):
    print("True")
else:
    print("Flase")