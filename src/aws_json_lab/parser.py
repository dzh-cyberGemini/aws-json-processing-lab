import json
from pathlib import Path
from typing import Any


def load_json(path: str | Path) -> dict[str, Any]:
    """Load a JSON object from a file."""
    file_path = Path(path)

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("Expected the root JSON value to be an object.")

    return data


def extract_instances(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract EC2 instances from AWS-style Reservations data."""
    instances: list[dict[str, Any]] = []

    for reservation in data.get("Reservations", []):
        if not isinstance(reservation, dict):
            continue

        for instance in reservation.get("Instances", []):
            if isinstance(instance, dict):
                instances.append(instance)

    return instances
