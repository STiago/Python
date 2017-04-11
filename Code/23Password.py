#!env/bin/python
import string
import random

def password_generator(n):
	chars=string.ascii_letters + string.digits + string.punctuation
	return ''.join(random.choice(chars) for _ in range(n))



def main():
    print "Number of characters in your password?"
    n = input()

    result = password_generator(n)

    print "The new password is: " + result

	#print(password_generator(int(input('Number of characters in your password?'))))

if __name__ == "__main__":
    main()
