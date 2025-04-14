from fastapi import APIRouter, Depends, HTTPException, status




orderitem_router = APIRouter(
    prefix="/orderitems"
)


@orderitem_router.get("/")
async def read_orderitems():
    pass

@orderitem_router.get("/{user_username}")
async def read_orderitem():
    pass

@orderitem_router.post("/")
async def create_orderitem():
    pass

@orderitem_router.put("/")
async def full_update_orderitem():
    pass

@orderitem_router.patch("/")
async def update_orderitem():
    pass

@orderitem_router.delete("/")
async def delete_orderitem():
    pass
