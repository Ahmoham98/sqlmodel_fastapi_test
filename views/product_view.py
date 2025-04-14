from fastapi import APIRouter, Depends, HTTPException, status




product_router = APIRouter(
    prefix="/products"
)


@product_router.get("/")
async def read_products():
    pass

@product_router.get("/{user_username}")
async def read_product():
    pass

@product_router.post("/")
async def create_product():
    pass

@product_router.put("/")
async def full_update_product():
    pass

@product_router.patch("/")
async def update_product():
    pass

@product_router.delete("/")
async def delete_product():
    pass
