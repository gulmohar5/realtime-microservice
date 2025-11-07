from fastapi import FastAPI

# Create the FastAPI app instance
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world! Your FastAPI server is running 🎉"}

@app.get("/publish")
def publish():
    return {"status": "Message published"}

@app.get("/subscribe")
def subscribe():
    return {"status": "Subscribed successfully"}
