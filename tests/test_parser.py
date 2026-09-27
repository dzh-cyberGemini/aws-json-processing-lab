from aws_json_lab.parser import extract_instances


def test_extract_instances() -> None:
    data = {
        "Reservations": [
            {
                "Instances": [
                    {"InstanceId": "i-001"},
                    {"InstanceId": "i-002"},
                ]
            }
        ]
    }

    result = extract_instances(data)

    assert len(result) == 2
    assert result[0]["InstanceId"] == "i-001"


def test_extract_instances_with_missing_reservations() -> None:
    assert extract_instances({}) == []
