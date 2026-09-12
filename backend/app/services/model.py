from pathlib import Path


class ModelService:
    """Small boundary for a future Keras model; never fabricates a prediction."""

    def __init__(self, model_path: Path):
        self.model_path = model_path

    @property
    def available(self) -> bool:
        return self.model_path.is_file()

    def placeholder(self) -> dict:
        return {
            "status": "model_unavailable",
            "message": "No trained model is installed yet. Add a compatible Keras artifact to enable diagnosis.",
            "next_steps": [
                "Capture a clear photo of the affected leaf in daylight.",
                "Ask a local agriculture expert to verify symptoms before treatment.",
            ],
        }
