import json
import sys
from jsonschema import validate, ValidationError

def main():
    with open("schema.json", "r") as schema_file:
        schema = json.load(schema_file)

    with open("sample.json", "r") as json_file:
        data = json.load(json_file)

    try:
        validate(instance=data, schema=schema)
        print("✅ JSON is valid.")
    except ValidationError as e:
        print("❌ JSON validation failed:")
        print(e.message)
        sys.exit(1)

if __name__ == "__main__":
    main()
