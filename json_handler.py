import json

def load_from_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["patients"]

def save_to_json(data, file_path):
    with open(file_path, "w") as f:
        json.dump({"patients": data}, f, indent=2)
