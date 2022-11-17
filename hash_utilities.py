import bcrypt
import sys
import errno

def generate_password_hash(password: str, salt_rounds: int) -> str:
    if(salt_rounds < 10 and salt_rounds > 20):
        print('Salt rounds must be in range [10,20]')
        sys.exit(errno.EINVAL)
    else:
        print('Salt rounds: ',salt_rounds)
        password_encoded = password.encode('utf-8')
        print('Coded password: ',password_encoded)
        seed = bcrypt.gensalt(salt_rounds)
        print('Seed: ',seed)
        hashed = bcrypt.hashpw(password_encoded,seed)
        print('Coded and hashed password: ',hashed)
        return hashed

def password_hash_check(password: str, hash: str) -> bool: 
    password_encoded = password.encode('utf-8')
    hash_encoded = hash.encode('utf-8')
    print('Coded password: ',password_encoded)
    print('Coded Hash: ',hash_encoded)

    return bcrypt.checkpw(password_encoded,hash_encoded)


if __name__ == '__main__':
    import sys
    try:
        password = sys.argv[1]
        pwd_hash = sys.argv[2]
        
        if( password_hash_check(password=password,hash=pwd_hash)):
            print('Password match')
        else:
            print('Password mismatch')
    
    except Exception as e:
        print(e)    