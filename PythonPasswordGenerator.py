import string
import secrets

def generate_password(numchar=8):
	alphabet = string.ascii_letters + string.digits + string.punctuation
	while True:
		password = ''.join(secrets.choice(alphabet) for i in range(numchar))
		if (any(c.islower() for c in password)
				and any(c.isupper() for c in password)
				and any(c.islower() for c in password)
				and any(c.isdigit() for c in password)
				and any([ch in string.punctuation for ch in password])):
			return(password)

generate_password(15)
