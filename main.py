import uvicorn

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from routers import candidate, positions

app = FastAPI()
app.include_router(candidate.router)
app.include_router(positions.router)

@app.get("/")
def home():
    return JSONResponse({"status":"Good"},status_code=status.HTTP_200_OK)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
