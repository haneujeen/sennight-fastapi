from fastapi import APIRouter

router = APIRouter()


@router.get("/factors")
async def get_factors():
    return {"message": "This is a protected endpoint"}
