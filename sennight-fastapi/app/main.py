from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from .database import engine, Base
from .routes import users, factors

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(factors.router)


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
    uvicorn.run(app, host="0.0.0.0", port=8000)
