from fastapi import APIRouter, Depends, HTTPException, status




category_router = APIRouter(
    prefix="/categories"
)


@category_router.get("/")
async def read_categories():
    pass

@category_router.get("/{user_username}")
async def read_category():
    pass

@category_router.post("/")
async def create_category():
    pass

@category_router.put("/")
async def full_update_category():
    pass

@category_router.patch("/")
async def update_category():
    pass

@category_router.delete("/")
async def delete_category():
    pass
