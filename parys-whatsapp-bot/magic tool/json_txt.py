import json
import os

def json_to_txt(json_path, txt_path):
    with open(json_path, "r") as f:
        services = json.load(f)

    with open(txt_path, "w") as f:
        for s in services:
            for key, value in s.items():
                if isinstance(value, bool) and key == "sponsored":
                    value = "yes" if value else "no"
                f.write(f"{key}: {value}\n")
            f.write("\n")

    print(f"✅ Converted {json_path} into {txt_path}")

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_to_txt(
        os.path.join(base_path, "services.json"),
        os.path.join(base_path, "services.txt")
    )