from mapper import map_transaction_to_word_tags


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
print(result)