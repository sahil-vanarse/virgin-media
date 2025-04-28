# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from research_data import research_data

app = FastAPI(title="Anapan AI Assignment - Research API", version="1.0")


class ResearchRequest(BaseModel):
    target_company: str
    competitors: List[str]


@app.post("/research")
def find_collaborations(request: ResearchRequest):
    result = {}

    for competitor in request.competitors:
        if competitor in research_data:
            result[competitor] = research_data[competitor]

    return {
        "target_company": request.target_company,
        "matched_competitors": result
    }
