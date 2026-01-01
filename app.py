from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EchoInput(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Web service is running successfully"}

@app.get("/health")
def health():
    return {"status": "healthy"}
@app.post("/echo")
def echo(data:EchoInput):
    return {"you sent: ",data.message}
