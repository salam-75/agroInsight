from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .schemas import AdvisoryItem, AdvisoryResponse, HealthResponse, PredictionResponse
from .services.model import ModelService

settings = get_settings()
model_service = ModelService(settings.model_path)

app = FastAPI(title="AgroInsight API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        model_available=model_service.available,
        model_path=str(model_service.model_path),
    )


@app.post("/api/v1/predictions", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)) -> PredictionResponse:
    if file.content_type not in {"image/jpeg", "image/png", "image/webp"}:
        raise HTTPException(status_code=415, detail="Upload a JPEG, PNG, or WebP image.")
    content = await file.read(settings.max_upload_bytes + 1)
    if len(content) > settings.max_upload_bytes:
        raise HTTPException(status_code=413, detail="Image must be 10 MB or smaller.")
    if not content:
        raise HTTPException(status_code=400, detail="The uploaded image is empty.")
    # Model inference will be wired here after training and validation.
    return PredictionResponse(**model_service.placeholder())


@app.get("/api/v1/advisories", response_model=AdvisoryResponse)
def advisories() -> AdvisoryResponse:
    return AdvisoryResponse(
        items=[
            AdvisoryItem(
                id="scouting",
                title="Scout before treating",
                body="Inspect several plants and both sides of affected leaves before deciding on treatment.",
                category="general",
            )
        ]
    )
