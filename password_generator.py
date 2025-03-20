import secrets
import string

def password_generator(pw_length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(pw_length))
    return password

if __name__ == "__main__":
    print(password_generator())