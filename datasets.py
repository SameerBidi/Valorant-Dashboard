import json

def get_weapons_dataset_as_dict():
  with open("static/datasets/weapons.json", "r") as weapons_file:
    data_json = weapons_file.read()

    data = json.loads(data_json)

    return data