import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api import api_router
from app.core.config import settings
from app.services.exceptions import register_exception_handlers
from logging_settings.logs_setup import setup_logging

# setup_logging()
log = logging.getLogger(__name__)
app = FastAPI()
app.include_router(api_router)
register_exception_handlers(app)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

log.info(f'Добавляем CORS_ORIGINS: {settings.CORS_ORIGINS}')

if __name__ == '__main__':
    log.info(f'Запускаем приложение: {settings.DEPLOY_HOST}:{settings.DEPLOY_PORT}')
    uvicorn.run(app, host=settings.DEPLOY_HOST, port=settings.DEPLOY_PORT)
