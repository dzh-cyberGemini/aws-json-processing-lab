import argparse

from .aggregators import count_by_instance_type
from .parser import extract_instances, load_json


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Process AWS CLI-style JSON data."
    )
    parser.add_argument("file", help="Path to the JSON file")
    args = parser.parse_args()

    data = load_json(args.file)
    instances = extract_instances(data)

    print(f"Instances: {len(instances)}")
    print("By instance type:")

    for instance_type, count in count_by_instance_type(instances).items():
        print(f"  {instance_type}: {count}")


if __name__ == "__main__":
    main()
