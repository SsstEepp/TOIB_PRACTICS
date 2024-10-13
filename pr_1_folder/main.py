import hashlib

def passwd_hasher():
    passwd = input(print("Enter password: "))
    passwd = bytes(passwd, 'utf-8')
    hash = hashlib.sha256(passwd)
    result = hash.hexdigest()
    return print(result)

if __name__ == "__main__":
    while True:
        passwd_hasher()
