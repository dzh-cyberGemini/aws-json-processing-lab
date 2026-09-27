from aws_json_lab.aggregators import count_by_instance_type, group_by_state


def test_count_by_instance_type() -> None:
    instances = [
        {"InstanceType": "t3.micro"},
        {"InstanceType": "t3.micro"},
        {"InstanceType": "t3.medium"},
    ]

    assert count_by_instance_type(instances) == {
        "t3.micro": 2,
        "t3.medium": 1,
    }


def test_group_by_state() -> None:
    instances = [
        {"InstanceId": "i-001", "State": {"Name": "running"}},
        {"InstanceId": "i-002", "State": {"Name": "stopped"}},
        {"InstanceId": "i-003", "State": {"Name": "running"}},
    ]

    result = group_by_state(instances)

    assert len(result["running"]) == 2
    assert len(result["stopped"]) == 1
