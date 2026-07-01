# FastAPI Clean Architecture

A FastAPI application following Clean Architecture principles with Domain-Driven Design patterns.

## Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Alembic** - Database migration tool
- **PostgreSQL** - Database
- **Pydantic** - Data validation using Python type annotations
- **python-jose** - JWT token handling
- **pwdlib** - Password hashing with Argon2
- **pytest** - Testing framework

## Architecture

This project follows Clean Architecture with the following layers:

- **Domain Layer** (`app/domain/`) - Business entities and repository interfaces
- **Application Layer** (`app/application/`) - Use cases and business logic
- **Infrastructure Layer** (`app/infrastructure/`) - Database models and repository implementations
- **API Layer** (`app/api/`) - REST API endpoints and routers

## Setup Instructions

### Prerequisites

- Python 3.14+
- PostgreSQL database
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd py-fastapi
```

2. Install dependencies:
```bash
uv sync
```

3. Create a `.env` file in the root directory:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_DAY=1
```

4. Run database migrations:
```bash
uv run alembic upgrade head
```

### Running the Application

#### Development Mode

```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

#### API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Database Migrations

Create a new migration:
```bash
uv run alembic revision --autogenerate -m "description"
```

Apply migrations:
```bash
uv run alembic upgrade head
```

Rollback migration:
```bash
uv run alembic downgrade -1
```

### Running Tests

```bash
uv run pytest
```

Run with coverage:
```bash
uv run pytest --cov=app --cov-report=html
```

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login user

### Profile
- `POST /api/v1/profiles/` - Create profile (requires auth)
- `GET /api/v1/profiles/me` - Get current user's profile (requires auth)
- `PUT /api/v1/profiles/me` - Update profile (requires auth)
- `DELETE /api/v1/profiles/me` - Delete profile (requires auth)

### Interests
- `POST /api/v1/interests/` - Create interest
- `GET /api/v1/interests/` - List all interests
- `GET /api/v1/interests/{id}` - Get interest by ID
- `PUT /api/v1/interests/{id}` - Update interest
- `DELETE /api/v1/interests/{id}` - Delete interest

### Health Check
- `GET /health` - Health check endpoint

## Project Structure

```
py-fastapi/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── routes/
│   │       │   ├── auth_router.py
│   │       │   ├── profile_router.py
│   │       │   └── interest_router.py
│   │       └── api.py
│   ├── application/
│   │   └── services/
│   │       ├── auth/
│   │       └── profile/
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── dependencies.py
│   │   └── exceptions/
│   ├── domain/
│   │   ├── entities/
│   │   └── repositories/
│   ├── infrastructure/
│   │   ├── database/
│   │   ├── db/
│   │   │   ├── models/
│   │   │   └── mixins/
│   │   └── repositories/
│   ├── schemas/
│   └── main.py
├── alembic/
├── tests/
│   ├── unit/
│   └── integration/
├── .env
├── pyproject.toml
└── README.md
```

## Development Guidelines

### Code Style
- Follow PEP 8 style guide
- Use type hints for all functions
- Keep functions small and focused

### Testing
- Write unit tests for services
- Write integration tests for API endpoints
- Aim for high test coverage

### Security
- Never commit `.env` files
- Use environment variables for sensitive data
- All passwords are hashed using Argon2
- JWT tokens for authentication

## License

[Your License Here]
