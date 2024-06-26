from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
from .database import engine, Base
from .routes import logs
from .config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(logs.router)


@app.middleware("http")
async def jwt_middleware(request: Request, call_next):
    authorization: str = request.headers.get("Authorization")
    if authorization is None or not authorization.startswith("Bearer "):
        return JSONResponse(
            status_code=401,
            content={"status": False, "detail": "Unauthorized", "data": None}
        )

    token = authorization[7:]
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise JWTError()
        request.state.user_id = user_id

    except JWTError as e:
        print(f"JWTError: {e}")
        return JSONResponse(
            status_code=401,
            content={"status": False, "detail": "Invalid token", "data": None}
        )

    return await call_next(request)


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": False,
            "detail": exc.detail,
            "data": None
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
