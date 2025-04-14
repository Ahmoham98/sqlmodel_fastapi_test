from fastapi import APIRouter, Depends, HTTPException, status




order_router = APIRouter(
    prefix="/orders"
)


@order_router.get("/")
async def read_orders():
    pass

@order_router.get("/{user_username}")
async def read_order():
    pass

@order_router.post("/")
async def create_order():
    pass

@order_router.put("/")
async def full_update_order():
    pass

@order_router.patch("/")
async def update_order():
    pass

@order_router.delete("/")
async def delete_order():
    pass
