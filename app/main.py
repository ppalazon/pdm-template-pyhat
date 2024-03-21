import subprocess
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import Settings
from app.routes import router

settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Context manager for FastAPI app. It will run all code before `yield`
    on app startup, and will run code after `yield` on app shutdown.
    """

    print("Starting this application...")
    print(
        "Don't forget to run tailwindcss with `pdm run tailwind` on any other terminal"
    )

    yield

    print("Finishing this application...")


def get_app() -> FastAPI:
    """Create a FastAPI app with the specified settings."""

    app = FastAPI(lifespan=lifespan, **settings.fastapi_kwargs)
    app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")
    app.include_router(router)
    return app


app = get_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
