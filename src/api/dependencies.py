from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from security import decode_token, get_current_user

auth_scheme = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    try:
        token = credentials.credentials
        payload = decode_token(token)
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
        return username
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

async def get_current_active_user(current_user: str = Depends(get_current_user)):
    # Implement additional logic to check if the user is active or has necessary permissions
    return current_user
