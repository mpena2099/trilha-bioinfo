from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SNPInput(BaseModel):
    rs123: int
    rs456: int

@app.post("/prever")
def prever(input: SNPInput):
    risco = 0.3 if input.rs123 == 1 else 0.7
    return {"risco": risco}
