from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from config import settings

from contextlib import asynccontextmanager

from views.user_view import user_router
from views.product_view import product_router
from views.orders_view import order_router
from views.orderitems_view import orderitem_router
from views.category_view import category_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(
    title="Online_pharmacy_service",
    description="Online pharmacy for save time and faster reach, anytime anywhere",
    version="1.0.0",
    lifespan=lifespan
)



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


# for dependency injection...
async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    
    async with async_session() as session:
        yield session




app.include_router(user_router, tags=["Users"])
app.include_router(product_router, tags=["Product"])
app.include_router(order_router, tags=["Orders"])
app.include_router(orderitem_router, tags=["Orderitems"])
app.include_router(category_router, tags=["categories"])