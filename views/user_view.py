from fastapi import APIRouter, Depends, HTTPException, status




user_router = APIRouter(
    prefix="/users"
)



@user_router.get("/")
async def read_users():
    pass

@user_router.get("/{user_username}")
async def read_user():
    pass

@user_router.post("/")
async def create_user():
    pass

@user_router.put("/")
async def full_update_user():
    pass

@user_router.patch("/")
async def update_user():
    pass

@user_router.delete("/")
async def delete_user():
    pass
