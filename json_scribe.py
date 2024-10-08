"""Contains functions for writing JSON files with a particular format."""

from pathlib import Path
import json
from typing import Any, Optional


def write_json_file(json_data: Any, json_file_path: Path, indent: Optional[int] = 4) -> None:
    """Write JSON data to a file at the given path. """
    with json_file_path.open('w', encoding='utf8') as json_file:
        json.dump(json_data, json_file, indent=indent)


def create_function_call_schema(
    function_name: str,
    function_description: str,
    parameters: dict[str, dict[str, Any]],
    required_parameters: list[str]
) -> list[dict[str, Any]]:
    """Create a JSON schema for a function call to an API.

    Args:
        function_name: The name of the function.
        function_description: A description of the function.
        parameters: A dictionary of parameters with their types and descriptions.
        required_parameters: A list of required parameter names.

    Returns:
        The JSON schema for the function call.
    """
    schema = {
        "name": function_name,
        "description": function_description,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": required_parameters
        }
    }

    for param_name, param_info in parameters.items():
        schema["parameters"]["properties"][param_name] = {
            "type": param_info["type"],
            "description": param_info["description"],
            "default": param_info.get("default", None)
        }

    return [schema]


def main():
    function_name = "example_function"
    function_description = "An example function that does something."
    parameters = {
        "param1": {
            "type": "string",
            "description": "A string parameter."
        },
        "param2": {
            "type": "integer",
            "description": "An integer parameter.",
            "default": 42
        }
    }
    required_parameters = ["param1"]

    schema = create_function_call_schema(
        function_name, function_description, parameters, required_parameters
    )

    json_file_path = Path("example_function_schema.json")
    write_json_file(schema, json_file_path)


if __name__ == "__main__":
    main()

