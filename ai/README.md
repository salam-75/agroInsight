# AI training scaffold

This directory documents a reproducible starting point for crop disease classification. It is **not a trained model** and the backend safely reports `model_unavailable` until a model artifact is created.

## Dataset contract

Place images in class folders (do not commit the dataset):

```text
ai/data/
├── train/<class-name>/*.jpg
└── validation/<class-name>/*.jpg
```

Use representative, licensed images with reliable labels. Keep a held-out test set outside training and record crop, disease, source, and capture conditions. Review class balance and label quality before deployment.

## Training

```bash
pip install -r requirements.txt
python train.py --data-dir data --output models/agroinsight_mobilenetv2.keras
```

The script uses MobileNetV2 transfer learning, freezes the base model initially, and writes class names beside the model. Tune augmentation, thresholds, and validation only after measuring performance on a held-out set.
