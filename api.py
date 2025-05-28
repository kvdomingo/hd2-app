from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from slowapi.errors import RateLimitExceeded

from src.lib.rate_limit import limiter, rate_limit_exceeded_handler
from src.routers import planets, warbonds

app = FastAPI(
    title="HD2 API",
    root_path="/api",
    docs_url="/docs",
    redoc_url="/redoc",
    default_response_class=ORJSONResponse,
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
@limiter.limit("100/minute")
async def health(request: Request):
    return {
        "api": "ok",
        "cache": "ok",
    }


app.include_router(planets.router)
app.include_router(warbonds.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
