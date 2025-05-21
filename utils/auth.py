from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "HIpotato"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
# Hash the user's password using bcrypt
def hash_password(password: str) -> str:
    return pwd_context.hash(password)
# Verify the password against the hashed version
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
# Create a JWT access token for authenticated users.
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)