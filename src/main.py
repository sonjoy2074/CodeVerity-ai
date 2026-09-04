from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is running!"}

if __name__ == "__main__":
    # Must specify 'src.main:app' so ASGI can locate the module
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000)