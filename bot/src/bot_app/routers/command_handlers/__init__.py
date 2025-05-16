__all__ = ('router',)

from aiogram import Router

from .start_handler import router as start_command_router
from .api_handler import router as api_handler
from .help_handler import router as help_command_router

router = Router(name=__name__)

router.include_routers(
    start_command_router,
    api_handler,
    help_command_router,
)
