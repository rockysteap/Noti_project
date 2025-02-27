__all__ = ('router',)

from aiogram import Router

from .start_handler import router as start_command_router
from .api_handler import router as api_handler

router = Router(name=__name__)

router.include_routers(
    start_command_router,
    api_handler,
)
