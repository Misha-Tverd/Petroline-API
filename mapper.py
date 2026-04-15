from datetime import datetime


def format_datetime(iso_date: str) -> str:
    if not iso_date:
        return ""

    dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
    return dt.strftime("%d.%m.%Y %H:%M")


def format_liters(value) -> str:
    if value is None:
        return ""
    return f"{float(value):.2f}"


def format_amount(value) -> str:
    if value is None:
        return ""
    return f"{float(value):.2f} грн"


def map_transaction_to_word_tags(transaction: dict) -> dict:
    return {
        "date": format_datetime(transaction.get("date", "")),
        "driver": transaction.get("personName", ""),
        "vehicle": transaction.get("transportName", ""),
        "fuel": transaction.get("fuelName", ""),
        "liters": format_liters(transaction.get("valueLitr")),
        "amount": format_amount(transaction.get("value")),
        "azs": transaction.get("azsName", ""),
        "transaction_id": str(transaction.get("id", "")),
    }