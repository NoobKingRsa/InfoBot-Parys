import json
import os

def txt_to_json(txt_path, json_path):
    with open(txt_path, "r") as f:
        lines = f.read().strip().split("\n")

    services = []
    current = {}

    for line in lines:
        if line.strip() == "":
            if current:
                # Convert 'yes'/'no' to boolean for sponsored
                if "sponsored" in current:
                    current["sponsored"] = current["sponsored"].strip().lower() == "yes"
                services.append(current)
                current = {}
        else:
            key, value = line.split(":", 1)
            current[key.strip()] = value.strip()

    if current:
        if "sponsored" in current:
            current["sponsored"] = current["sponsored"].strip().lower() == "yes"
        services.append(current)

    with open(json_path, "w") as f:
        json.dump(services, f, indent=2)

    print(f"✅ Converted {txt_path} into {json_path}")

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    txt_to_json(
        os.path.join(base_path, "services.txt"),
        os.path.join(base_path, "services.json")
    )