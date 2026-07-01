import bcrypt

def hash_password(password: str) -> str:
    # Truncate to 72 bytes if needed (bcrypt limit)
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
    
    # Generate salt and hash
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    
    # Return as string for database storage
    return hashed.decode('utf-8')
def verify_password(plain: str, hashed: str) -> bool:
    # Truncate plain password to 72 bytes if needed
    plain_bytes = plain.encode('utf-8')
    if len(plain_bytes) > 72:
        plain_bytes = plain_bytes[:72]
    
    # Hash is stored as string in DB, convert to bytes
    hashed_bytes = hashed.encode('utf-8')
    
    # Verify
    return bcrypt.checkpw(plain_bytes, hashed_bytes)