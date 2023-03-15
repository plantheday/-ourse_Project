import pytest

from utils import get_data, get_last_data, get_formatted_data, get_filtered_data

def test_get_data():
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678878629852&signature=dEuS7Wt9bJtuwkyGbyEMO455OD_Vvi4EqXA39JtuSdE&downloadName=operations.json"
    assert get_data(url) is not None
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678878629852&signature=dEuS7Wt9bJtuwkyGbyEMO455OD_Vvi4EqXA39JtuSdE&downloaName=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "WARNING: Статус ответа 400"
    url = "https://fil.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678878629852&signature=dEuS7Wt9bJtuwkyGbyEMO455OD_Vvi4EqXA39JtuSdE&downloadName=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "ERROR: requests.exceptions.ConnectionError"


def test_get_last_data(test_data):
    data = get_last_data(test_data, count_last_values=2)
    assert data[0]['date'] == '2021-04-04T23:20:05.206878'
    assert len(data) == 2

def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:1])
    assert data == ['06.09.2019 Перевод организации\nVisa Gold 3654 41** **** 1 -> Счет **8289\n6357.56 USD\n']
    data = get_formatted_data(test_data[1:2])
    print(data)
    assert data == ['20.06.2018 Перевод с карты на счет\n[СКРЫТО]  -> Счет **3980\n96350.51 USD\n']

def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 9
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 7

