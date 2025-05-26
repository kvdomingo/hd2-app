from fastapi import FastAPI

app = FastAPI(
    title="HD2 API",
    root_path="/api",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
