from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from config import settings


#async engine
async_engine = create_async_engine(
    url = settings.DATABASE_URL,
    echo = True
)


async def init_db():
    async with async_engine.begin() as conn:
        from models.users_model import Users
        from models.category_model import Categories
        from models.product_model import Products
        from models.order_model import Orders
        from models.orderitem_model import OrderItems
        await conn.run_sync(SQLModel.metadata.create_all)


#dependency injection code
@app.get("/ping")
async def root_response():
    return {"message": "pong"}