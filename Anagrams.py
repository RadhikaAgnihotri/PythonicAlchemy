#Valid Anagrams Leetcode 242

# class Solution:
#   def isAnagram(self, s: str, t: str) -> bool:
#     if (sorted(s) == sorted(t)):
#       return True

#Solution from scratch
word_1 = input("Please enter the 1st word :")
word_2 = input("Please enter the 2nd word :")
new_word_1 = word_1.lower() #to handle case sensitivity
new_word_2 = word_2.lower() #to convert all letters in lowercase then compare
if (sorted(new_word_1) == sorted(new_word_2)):
    print(word_1,"is a valid anagram of" ,word_2, "or vice versa")
else:
    print(word_1,"is not a valid anagram of",word_2,"or vice-versa")    