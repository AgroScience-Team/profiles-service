from typing import Any
from fastapi import Depends, HTTPException, Query, status
from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError

from src.schemas.token import TokenPayloadSchema
from src.utils.roles import RoleEnum


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/profiles/organizations/token")


class Token:
    @staticmethod
    def get_payload(token: str = Depends(oauth2_scheme)) -> TokenPayloadSchema:
        try:
            payload = jwt.get_unverified_claims(token)
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return TokenPayloadSchema.model_validate(payload)

    @staticmethod
    def get_organization_payload(
        token_payload: TokenPayloadSchema = Depends(get_payload)
    ) -> TokenPayloadSchema:
        if token_payload.role != RoleEnum.ORGANIZATION.value:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not an organization"
            )
        return token_payload

    @staticmethod
    def get_worker_payload(
        token_payload: TokenPayloadSchema = Depends(get_payload)
    ) -> TokenPayloadSchema:
        if token_payload.role != RoleEnum.WORKER.value:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not a worker"
            )
        return token_payload
    
    @staticmethod
    def get_organization_viewer(
        user_id: int = Query(...),
        token_payload: TokenPayloadSchema = Depends(get_payload)
    ) -> TokenPayloadSchema:
        if token_payload.org != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"You are not a member of organization: {user_id}"
            )
        return token_payload
