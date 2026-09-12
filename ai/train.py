"""MobileNetV2 transfer-learning scaffold; requires a real class-folder dataset."""
import argparse
import json
from pathlib import Path

import tensorflow as tf


def build_model(class_count: int, image_size: tuple[int, int] = (224, 224)) -> tf.keras.Model:
    base = tf.keras.applications.MobileNetV2(
        input_shape=(*image_size, 3), include_top=False, weights="imagenet"
    )
    base.trainable = False
    inputs = tf.keras.Input(shape=(*image_size, 3))
    x = tf.keras.applications.mobilenet_v2.preprocess_input(inputs)
    x = base(x, training=False)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dropout(0.2)(x)
    outputs = tf.keras.layers.Dense(class_count, activation="softmax")(x)
    model = tf.keras.Model(inputs, outputs)
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    train_dir = args.data_dir / "train"
    validation_dir = args.data_dir / "validation"
    if not train_dir.is_dir() or not validation_dir.is_dir():
        raise SystemExit("Expected data/train and data/validation class folders.")
    train = tf.keras.utils.image_dataset_from_directory(train_dir, image_size=(224, 224), batch_size=32)
    validation = tf.keras.utils.image_dataset_from_directory(
        validation_dir, image_size=(224, 224), batch_size=32, shuffle=False, class_names=train.class_names
    )
    model = build_model(len(train.class_names))
    model.fit(train, validation_data=validation, epochs=5)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    model.save(args.output)
    args.output.with_suffix(".classes.json").write_text(json.dumps(train.class_names, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
