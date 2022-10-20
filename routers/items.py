from fastapi import APIRouter

router=APIRouter()


@router.get("/items",tags=["Items"])
async def read_items():
    return [{"message": "hello Users"}]

@router.post("/items",tags=["Items"])
async def create_items():
    return [{"message": "Create Users"}]