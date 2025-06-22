import json
import os

REQUIRED_FIELDS = ["type", "name", "phone", "location", "note", "sponsored"]

def verify_services(path):
    with open(path, "r") as f:
        data = json.load(f)

    errors = []
    for i, entry in enumerate(data):
        for field in REQUIRED_FIELDS:
            if field not in entry:
                errors.append(f"❌ Entry {i+1} missing field: {field}")
    
    if errors:
        print("⚠️  Verification failed:\n")
        print("\n".join(errors))
    else:
        print("✅ All services passed verification!")

if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base, "services.json")
    verify_services(file_path)