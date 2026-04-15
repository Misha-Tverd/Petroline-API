CRITICAL_FIELDS = [
    "driver",
    "vehicle",
    "liters",
    "date",
    "liters"
]

def validate_required_fields(mapped_data: dict) -> tuple[bool, list]:
    missing_fields = []

    for field in CRITICAL_FIELDS:
        value = mapped_data.get(field)

        if value is None or value == "":
            missing_fields.append(field)
    is_valid = len(missing_fields) == 0

    return is_valid, missing_fields