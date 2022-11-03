import json

def process_weapons_data():
  data = []
  with open("static/datasets/weapons_raw.json", "r") as weapons_raw_file:
    raw_data = json.load(weapons_raw_file)
    for weaponRaw in raw_data["data"][:17]:
      data.append({
        "displayName": weaponRaw["displayName"],
        "category": weaponRaw["category"].split("::")[1],
        "displayIcon": weaponRaw["displayIcon"],
        "fireRate": weaponRaw["weaponStats"]["fireRate"],
        "magazineSize": weaponRaw["weaponStats"]["magazineSize"],
        "runSpeedMultiplier": weaponRaw["weaponStats"]["runSpeedMultiplier"],
        "equipTimeSeconds": weaponRaw["weaponStats"]["equipTimeSeconds"],
        "reloadTimeSeconds": weaponRaw["weaponStats"]["reloadTimeSeconds"],
        "firstBulletAccuracy": weaponRaw["weaponStats"]["firstBulletAccuracy"],
        "wallPenetration": weaponRaw["weaponStats"]["wallPenetration"].split("::")[1],
        "headDamageShort": weaponRaw["weaponStats"]["damageRanges"][0]["headDamage"],
        "bodyDamageShort": weaponRaw["weaponStats"]["damageRanges"][0]["bodyDamage"],
        "legDamageShort": weaponRaw["weaponStats"]["damageRanges"][0]["legDamage"],
        "headDamageFar": weaponRaw["weaponStats"]["damageRanges"][0]["headDamage"],
        "bodyDamageFar": weaponRaw["weaponStats"]["damageRanges"][0]["bodyDamage"],
        "legDamageFar": weaponRaw["weaponStats"]["damageRanges"][0]["legDamage"],
        "cost": weaponRaw["shopData"]["cost"],
        "skinCount": len(weaponRaw["skins"])
      })
  
  with open("static/datasets/weapons.json", "w") as weapons_file:
    weapons_file.write(json.dumps(data))
    weapons_file.close()
  

process_weapons_data()