from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from io import BytesIO

from agents.fx_standard.modules.fx_analyzer import analyze_standard_fx
from agents.fx_plus.modules.fx_analyzer import analyze_plus_fx
from agents.fx_premium.modules.fx_analyzer import analyze_premium_fx

app = FastAPI(title="FX Agent API", version="1.0")

@app.get("/")
def root():
    return {"message": "FX API is live. Use /analyze endpoint."}

@app.post("/analyze")
async def analyze_fx_file(file: UploadFile = File(...), agent: str = Form(...)):
    if not file.filename.endswith((".xls", ".xlsx")):
        raise HTTPException(status_code=400, detail="Only Excel files are allowed.")

    content = await file.read()
    df = pd.read_excel(BytesIO(content))

    if agent == "standard":
        result = analyze_standard_fx(df)
    elif agent == "plus":
        result = analyze_plus_fx(df)
    elif agent == "premium":
        result = analyze_premium_fx(df)
    else:
        raise HTTPException(status_code=400, detail="Invalid agent type.")

    return JSONResponse(content=result)
