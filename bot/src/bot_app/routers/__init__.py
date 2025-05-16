__all__ = ('router',)

from aiogram import Router

from src.bot_app.routers.command_handlers import router as commands_router
from src.bot_app.routers.root_menu import router as root_menu_router
from .default_handler import router as default_router

router = Router(name=__name__)

router.include_routers(
    commands_router,
    root_menu_router,
)

router.include_router(default_router)
