# agroInsight

AgroInsight is a mobile-first crop diagnosis starter with a FastAPI service, a React/Vite client, and a TensorFlow/Keras training scaffold. It intentionally does **not** claim to contain a trained model: the prediction API returns an explicit `model_unavailable` placeholder until a compatible artifact is installed.

## Repository layout

```text
agroInsight/
├── backend/      # FastAPI API and Pydantic schemas
├── frontend/     # React + Vite responsive web/mobile UI
├── ai/            # MobileNetV2 transfer-learning scaffold and dataset notes
└── .env.example
```

## Quick start

### Backend

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API is available at `http://localhost:8000`, with interactive docs at `/docs`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Set `VITE_API_BASE_URL` when the API is not running on the default `http://localhost:8000`.

### Training scaffold

See [`ai/README.md`](ai/README.md). The training script expects a class-folder dataset and writes a model only after a real training run. No model file is checked in.

## API endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/health` | Service and model availability |
| POST | `/api/v1/predictions` | Upload a leaf image for diagnosis (placeholder until a model exists) |
| GET | `/api/v1/advisories` | Return advisory scaffold data |

## Environment and safety

Copy `.env.example` to `.env` for local configuration. Uploaded images are validated by content type and size, and the current scaffold does not persist them. Predictions are educational placeholders, not agronomic, medical, or pesticide-use guarantees.
