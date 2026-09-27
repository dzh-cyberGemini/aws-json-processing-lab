from typing import Any


def tags_to_dict(tags: list[dict[str, Any]]) -> dict[str, str]:
    """Convert AWS-style tags into a simple dictionary."""
    result: dict[str, str] = {}

    for tag in tags:
        key = tag.get("Key")
        value = tag.get("Value")

        if isinstance(key, str) and isinstance(value, str):
            result[key] = value

    return result


def simplify_instance(instance: dict[str, Any]) -> dict[str, Any]:
    """Convert an AWS-style instance into a simplified representation."""
    tags = tags_to_dict(instance.get("Tags", []))

    return {
        "id": instance.get("InstanceId"),
        "type": instance.get("InstanceType"),
        "state": instance.get("State", {}).get("Name"),
        "environment": tags.get("Environment", "unknown"),
    }
