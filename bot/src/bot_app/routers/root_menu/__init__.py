__all__ = ('router',)

from aiogram import Router

from .root_menu_handler import router as root_menu_router

router = Router(name=__name__)

router.include_routers(
    root_menu_router,
)
