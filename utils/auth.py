from datetime import datetime, timedelta
from typing import Optional

from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Zeyad: seceret keys should be stored in environment variables
# or a secure vault in production
SECRET_KEY = "HIpotato"
ALGORITHM = "HS256"

########## Zeyad: access token should expire after a short time, like 15 minutes
# I can see you are already using 15 min, so this seems like a redundant variable
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# Hash the user's password using bcrypt
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# Verify the password against the hashed version
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


################# Zeyad: Optional needs to be used for None values
# also The method "utcnow" in class "datetime" is deprecated
# Create a JWT access token for authenticated users.
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
