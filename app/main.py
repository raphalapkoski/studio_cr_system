
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from app.core.database import Base, engine
from app.api.gym_member_routes import router as gym_member_router
from app.api.class_routes import router as class_router
from fastapi.exceptions import RequestValidationError

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gym System - Gym Members Management")

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"errors": [{"field": None, "message": str(exc)}]}
    )

@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [
        {
            "field": ".".join([str(loc) for loc in e["loc"][1:]]),  # ignora "body"
            "message": e["msg"]
        }
        for e in exc.errors()
    ]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"errors": errors}
    )
    
app.include_router(gym_member_router, prefix="/gym-members", tags=["Alunos"])
app.include_router(class_router, prefix="/classes", tags=["Aulas"])
