from aws_json_lab.filters import filter_by_state, filter_by_tag


def test_filter_by_state() -> None:
    instances = [
        {"InstanceId": "i-001", "State": {"Name": "running"}},
        {"InstanceId": "i-002", "State": {"Name": "stopped"}},
    ]

    result = filter_by_state(instances, "running")

    assert len(result) == 1
    assert result[0]["InstanceId"] == "i-001"


def test_filter_by_tag() -> None:
    instances = [
        {
            "InstanceId": "i-001",
            "Tags": [{"Key": "Environment", "Value": "production"}],
        },
        {
            "InstanceId": "i-002",
            "Tags": [{"Key": "Environment", "Value": "development"}],
        },
    ]

    result = filter_by_tag(instances, "Environment", "production")

    assert len(result) == 1
    assert result[0]["InstanceId"] == "i-001"
