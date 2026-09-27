# AWS JSON Processing Lab

A Python training and interview-preparation project focused on parsing, processing, filtering, transforming, and aggregating large nested JSON structures similar to AWS CLI output.

The primary goal is not simply to produce the correct result.

The goal is to demonstrate:

* structured problem solving
* clean Python code
* understanding of nested data structures
* defensive data handling
* appropriate use of Python data structures
* readable transformations
* testable code
* time and space complexity awareness

## Why this project exists

AWS CLI commands commonly return deeply nested JSON structures.

For example:

```text
Reservations
└── Instances
    ├── InstanceId
    ├── InstanceType
    ├── State
    ├── LaunchTime
    └── Tags
        ├── Key
        └── Value
```

This project uses AWS-style datasets to practice working with structures such as:

```python
dict[str, list[dict[str, object]]]
```

The exercises progressively increase in complexity.

## Learning objectives

By completing this repository, I should be able to:

1. Navigate deeply nested dictionaries and lists.
2. Safely access optional fields.
3. Filter records using multiple conditions.
4. Extract and normalize nested information.
5. Convert lists into dictionaries and lookup indexes.
6. Group records by one or more attributes.
7. Aggregate counts and other values.
8. Transform one JSON structure into another.
9. Sort nested records.
10. Handle missing and malformed data.
11. Separate data loading, processing, and presentation.
12. Write unit tests for data-processing functions.
13. Reason about time and space complexity.
14. Process larger datasets without unnecessary repeated traversal.
15. Explain implementation decisions clearly during an interview.

## Project philosophy

The preferred solution is:

```text
Input
  ↓
Parse
  ↓
Validate / normalize
  ↓
Filter
  ↓
Transform
  ↓
Aggregate
  ↓
Output
```

Solutions should prioritize:

* readability
* correctness
* predictable behavior
* testability
* appropriate data structures

Shorter code is not automatically better code.

For example, a complicated one-line comprehension should not be preferred over a clear loop if the loop makes the logic easier to understand.

## Project structure

```text
aws-json-processing-lab/
│
├── src/
│   └── aws_json_lab/
│       ├── models.py
│       ├── parser.py
│       ├── filters.py
│       ├── transformers.py
│       ├── aggregators.py
│       └── cli.py
│
├── tests/
│   ├── test_parser.py
│   ├── test_filters.py
│   ├── test_transformers.py
│   └── test_aggregators.py
│
├── data/
│   ├── ec2.json
│   └── ec2_large.json
│
└── exercises/
    ├── 01_basic_traversal.md
    ├── 02_filtering.md
    ├── 03_nested_data.md
    ├── 04_grouping.md
    ├── 05_transformation.md
    ├── 06_edge_cases.md
    ├── 07_large_dataset.md
    └── 08_interview_simulation.md
```

## Setup

Python 3.12+ is recommended.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project:

```bash
pip install -e .
```

Install development dependencies:

```bash
pip install -e ".[dev]"
```

## Running the project

Example:

```bash
python -m aws_json_lab.cli data/ec2.json
```

Or, once the CLI is implemented:

```bash
aws-json-lab data/ec2.json
```

## Testing

Run all tests:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_filters.py
```

## Code quality

The project is intended to use:

```text
Ruff
Pyright
Pytest
```

Run Ruff:

```bash
ruff check .
```

Run formatting:

```bash
ruff format .
```

Run type checking:

```bash
pyright
```

## Exercises

The exercises progress from basic traversal to interview-level problems.

### Level 1 — Basic traversal

Navigate nested dictionaries and lists.

### Level 2 — Filtering

Find records matching specific conditions.

### Level 3 — Nested data

Work with nested state, tags, network interfaces, and other AWS-style structures.

### Level 4 — Grouping

Group resources by instance type, environment, availability zone, or state.

### Level 5 — Transformation

Convert AWS-style structures into simpler application-specific structures.

### Level 6 — Edge cases

Handle:

* missing keys
* empty lists
* `None`
* missing tags
* duplicate records
* unexpected values

### Level 7 — Large datasets

Process larger JSON datasets while avoiding unnecessary repeated traversal.

### Level 8 — Interview simulation

Solve problems under time constraints without looking at previous solutions.

## Example problem

Given:

```json
{
  "Reservations": [
    {
      "Instances": [
        {
          "InstanceId": "i-001",
          "InstanceType": "t3.medium",
          "State": {
            "Name": "running"
          },
          "Tags": [
            {
              "Key": "Environment",
              "Value": "production"
            }
          ]
        }
      ]
    }
  ]
}
```

Produce:

```python
{
    "production": {
        "running": 1
    }
}
```

Then extend the solution to support:

* multiple reservations
* multiple instances
* missing tags
* stopped instances
* unknown environments
* multiple instance types

## Complexity

Each solution should consider:

```text
Time complexity
Space complexity
Number of passes over the data
```

For example, if a dataset contains `N` instances and each instance contains at most `T` tags:

```text
Scanning all instances: O(N)

Scanning every tag:
O(N × T)

Building a tag lookup dictionary:
O(T)

Tag lookup:
O(1) average
```

The objective is not to optimize everything prematurely.

The objective is to understand the trade-offs.

## Interview mindset

For every problem:

### 1. Understand

Identify:

* input structure
* required output
* constraints
* optional fields
* edge cases

### 2. Design

Before writing code:

```text
What data do I need?
What traversal is required?
Which data structure fits?
Can I solve this in one pass?
```

### 3. Implement

Write readable Python.

### 4. Test

Consider:

```text
normal input
empty input
missing fields
unexpected values
multiple records
```

### 5. Explain

Be able to explain:

* why the solution works
* why the chosen data structures were used
* time complexity
* space complexity
* possible improvements

## Progress tracking

| Area                     | Status |
| ------------------------ | ------ |
| Dictionary traversal     | ⬜      |
| List traversal           | ⬜      |
| Nested structures        | ⬜      |
| Filtering                | ⬜      |
| Sorting                  | ⬜      |
| Tag extraction           | ⬜      |
| Grouping                 | ⬜      |
| Aggregation              | ⬜      |
| Transformation           | ⬜      |
| Defensive access         | ⬜      |
| Error handling           | ⬜      |
| Type hints               | ⬜      |
| Unit testing             | ⬜      |
| Complexity analysis      | ⬜      |
| Large JSON processing    | ⬜      |
| Timed interview problems | ⬜      |

## Final objective

The final goal is to be able to receive an unfamiliar AWS-style JSON object and confidently answer:

> "What information do you need to extract, how would you structure the solution, and why?"

Then implement the solution cleanly without relying on trial-and-error.
