# AgroInsight API

The API is intentionally model-agnostic. `POST /api/v1/predictions` validates an image upload and returns `model_unavailable` while `MODEL_PATH` does not point to a trained Keras model. This makes the client usable during product development without presenting fabricated diagnoses.

Run from this directory with:

```bash
uvicorn app.main:app --reload
```
