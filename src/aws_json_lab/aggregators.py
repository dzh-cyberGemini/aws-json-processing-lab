from collections import Counter, defaultdict
from typing import Any


def count_by_instance_type(
    instances: list[dict[str, Any]],
) -> dict[str, int]:
    """Count instances by instance type."""
    counts: Counter[str] = Counter()

    for instance in instances:
        instance_type = instance.get("InstanceType")

        if isinstance(instance_type, str):
            counts[instance_type] += 1

    return dict(counts)


def group_by_state(
    instances: list[dict[str, Any]],
) -> dict[str, list[dict[str, Any]]]:
    """Group instances by state."""
    result: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)

    for instance in instances:
        state = instance.get("State", {}).get("Name", "unknown")
        result[state].append(instance)

    return dict(result)
