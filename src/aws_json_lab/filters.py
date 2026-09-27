from typing import Any


def filter_by_state(
    instances: list[dict[str, Any]],
    state: str,
) -> list[dict[str, Any]]:
    """Return instances matching the requested state."""
    return [
        instance
        for instance in instances
        if instance.get("State", {}).get("Name") == state
    ]


def filter_by_tag(
    instances: list[dict[str, Any]],
    key: str,
    value: str,
) -> list[dict[str, Any]]:
    """Return instances containing a matching tag."""
    result = []

    for instance in instances:
        for tag in instance.get("Tags", []):
            if (
                isinstance(tag, dict)
                and tag.get("Key") == key
                and tag.get("Value") == value
            ):
                result.append(instance)
                break

    return result
