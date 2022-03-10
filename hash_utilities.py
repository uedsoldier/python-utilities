import bcrypt
import sys
import errno

def generate_password_hash(password, salt_rounds):
    if(salt_rounds < 10 and salt_rounds > 20):
        print('Salt rounds deben estar en el rango [10,20]')
        sys.exit(errno.EINVAL)
    else:
        print('Salt rounds: ',salt_rounds)
        password_encoded = password.encode('utf-8')
        print('Password codificado: ',password_encoded)
        seed = bcrypt.gensalt(salt_rounds)
        print('Semilla (seed): ',seed)
        hashed = bcrypt.hashpw(password_encoded,seed)
        print('Password codificado y cifrado: ',hashed)
        return hashed

def password_hash_check(password, hash):
    password_encoded = password.encode('utf-8')
    hash_encoded = hash.encode('utf-8')
    print('Password codificado: ',password_encoded)
    print('Hash codificado: ',hash_encoded)

    if bcrypt.checkpw(password_encoded,hash_encoded):
        print('Password match!!')
        return True
    else:
        print('Password mismatch')
        return False