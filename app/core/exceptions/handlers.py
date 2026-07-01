from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions.base_exception import AppException


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(AppException)
    async def app_exception_handler(
        request: Request,
        exc: AppException,
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "message": exc.message,
            },
        )