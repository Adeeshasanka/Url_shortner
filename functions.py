import secrets
import string

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits #A-Z, a-z, 1-9
    return ''.join(secrets.choice(chars) for _ in range(length))



