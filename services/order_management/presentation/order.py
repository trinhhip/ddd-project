from fastapi import APIRouter
from ..domain.usecases.order_action import OrderAction
from ..domain.repository.order_repository import OrderRepository

router = APIRouter()

@router.post('/order/{order_id}')
async def order(order_id: str):
    order_repository = OrderRepository()
    return OrderAction(order_repository, order_id)