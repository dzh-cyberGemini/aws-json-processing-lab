from aws_json_lab.transformers import simplify_instance, tags_to_dict


def test_tags_to_dict() -> None:
    tags = [
        {"Key": "Environment", "Value": "production"},
        {"Key": "Team", "Value": "platform"},
    ]

    assert tags_to_dict(tags) == {
        "Environment": "production",
        "Team": "platform",
    }


def test_simplify_instance() -> None:
    instance = {
        "InstanceId": "i-001",
        "InstanceType": "t3.medium",
        "State": {"Name": "running"},
        "Tags": [{"Key": "Environment", "Value": "production"}],
    }

    assert simplify_instance(instance) == {
        "id": "i-001",
        "type": "t3.medium",
        "state": "running",
        "environment": "production",
    }
