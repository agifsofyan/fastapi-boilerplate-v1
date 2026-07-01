from fastapi import status

from app.core.exceptions.base_exception import AppException


class UserNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            message="User tidak ditemukan.",
            status_code=status.HTTP_404_NOT_FOUND,
        )


class EmailAlreadyExistsException(AppException):

    def __init__(self):
        super().__init__(
            message="Email sudah digunakan.",
            status_code=status.HTTP_409_CONFLICT,
        )
        
class UserAlreadyExistsException(AppException):
    
    def __init__(self):
        super().__init__(
            message="Pengguna sudah terdaftar.",
            status_code=status.HTTP_409_CONFLICT,
        )