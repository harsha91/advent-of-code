print("Advent of Code - DAY 1")

''' 
The captcha requires you to review a sequence of digits (your
puzzle input) and find the sum of all digits that match the next digit
in the list. The list is circular, so the digit after the last digit
is the first digit in the list.

For example:

- 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches 
 	the second digit and the third digit (2) matches the fourth digit.
- 1111 produces 4 because each digit (all 1) matches the next.
- 1234 produces 0 because no digit matches the next.
- 91212129 produces 9 because the only digit that matches the next 
	one is the last digit, 9.
'''

def breakCaptcha(payLoad):
	sum = i = prevNumber = 0
	numbers = str(payLoad)

	for i in numbers:
		if prevNumber == i:
			sum = sum + int(i)
		prevNumber = i

	if(int(numbers[0]) == int(repr(payLoad)[-1])) :
		sum = sum + int(numbers[0])
	print("And the Captcha is broken :: " + str(sum))

if __name__ == '__main__':
	problem = int(open('problems/1_day.txt','r').read())
	breakCaptcha(problem)