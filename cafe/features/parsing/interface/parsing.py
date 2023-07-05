from fastapi import APIRouter

router = APIRouter()

base_url = "/api/v1"

@router.get(base_url + "/parsing")
async def parsing():
    return {"message": "parsing"}