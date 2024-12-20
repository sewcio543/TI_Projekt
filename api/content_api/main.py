from fastapi import FastAPI, status
from sqlalchemy import text

import api.content_api.routers.comment_controller as comments
import api.content_api.routers.grudge_controller as grudges
import api.content_api.routers.post_controller as posts
from api import settings
from api.dependencies import dep
from api.shared.cors import add_cors_middleware

# from testing.helpers import seed_database

app = FastAPI(title="GrudgeHub Content API")
add_cors_middleware(
    app,
    origins=[
        settings.FRONTEND_URL,
        settings.PEOPLE_API_URL,
    ],
)
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(grudges.router)


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "oj bratku, działa"}


@app.get("/db_health", status_code=status.HTTP_200_OK)
async def db_health_check():
    async with dep.session as sess:
        cursor = await sess.execute(text("SELECT version()"))
        return f"Ok {cursor.one()[0]}"
