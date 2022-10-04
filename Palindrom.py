num = 1221
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")

  # # function which return reverse of a string

# def isPalindrome(s):
# 	return s == s[::-1]


# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)

# if ans:
# 	print("Yes")
# else:
# 	print("No")
