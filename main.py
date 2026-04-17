from mapper import map_transaction_to_word_tags
from validators import validate_required_fields
from storage import append_missing_record

sample_transaction = {
    "id": 123,
    "date": "2026-04-14T11:12:12.942Z",
    "personName": "Іван Петренко",
    "transportName": "John Deere 6195M AA1234BB",
    "fuelName": "ДП",
    "valueLitr": 125.4,
    "value": 5000,
    "azsName": "АЗС-1"
}

result = map_transaction_to_word_tags(sample_transaction)




is_valid, missing = validate_required_fields(result)

if not is_valid:
    append_missing_record(
        record_id=sample_transaction.get("id"),
        missing_fields=missing,
        raw_data=sample_transaction
    )
    print("Запис зберено в лог")
else:
    print("Все ок, можна створювати Word")

# Delete this comment sdf