import pytest

@pytest.fixture
def test_data():
    return [
        {
            "id": 736942989,
            "state": "EXECUTED",
            "date": "2019-09-06T00:48:01.081967",
            "operationAmount": {
                "amount": "6357.56",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 3654412434951162",
            "to": "Счет 59986621134048778289"
        },
        {
            "id": 580054042,
            "state": "EXECUTED",
            "date": "2018-06-20T03:59:34.851630",
            "operationAmount": {
                "amount": "96350.51",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "to": "Счет 86655182730188443980"
        },
        {
            "id": 619287771,
            "state": "EXECUTED",
            "date": "2019-08-19T16:30:41.967497",
            "operationAmount": {
                "amount": "81150.87",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 17691325653939384901",
            "to": "Счет 49304996510329747621"
        },
        {
            "id": 490100847,
            "state": "EXECUTED",
            "date": "2018-12-22T02:02:49.564873",
            "operationAmount": {
                "amount": "56516.63",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 8326537236216459",
            "to": "MasterCard 6783917276771847"
        },
        {
            "id": 179194306,
            "state": "EXECUTED",
            "date": "2019-05-19T12:51:49.023880",
            "operationAmount": {
                "amount": "6381.58",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "МИР 5211277418228469",
            "to": "Счет 58518872592028002662"
        },
        {
            "id": 27192367,
            "state": "CANCELED",
            "date": "2018-12-24T20:16:18.819037",
            "operationAmount": {
                "amount": "991.49",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 71687416928274675290",
            "to": "Счет 87448526688763159781"
        },
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2021-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "25780.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "to": "Счет 20735820461482021315"
        },
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
            "operationAmount": {
                "amount": "92688.46",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
        },
        {
            "id": 957763565,
            "state": "EXECUTED",
            "date": "2019-01-05T00:52:30.108534",
            "operationAmount": {
                "amount": "87941.37",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 46363668439560358409",
            "to": "Счет 18889008294666828266"
        },
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        }
    ]