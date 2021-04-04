from fastapi import APIRouter

from databaseinterface.api.endpoints.hello import hello_router
from databaseinterface.api.endpoints.setting import setting_router
from databaseinterface.api.endpoints.query import query_router


router = APIRouter()

router.include_router(hello_router, prefix="/hello")
router.include_router(setting_router, prefix="/setting")
router.include_router(query_router, prefix="/query")