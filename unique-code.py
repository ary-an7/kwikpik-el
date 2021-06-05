import re
def getNumbers(str):
	a = re.findall(r'[0-9]+', str)
	return a


str = input("Enter the Selfie name:")
a = getNumbers(str)
print("Unique Code is:")
print(*a)
