import json
from pathlib import Path

LOG_PATH = Path("logs/missing_fields_log.json")

def append_missing_record(record_id: int, missing_fields: list, raw_data: dict):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    # if file exists - read it
    if LOG_PATH.exists():
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

    else: 
        data = []
    
    # add a new entry
    data.append({
        "id": record_id,
        "missing_fields": missing_fields,
        "raw": raw_data
    })

    # rewind
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)