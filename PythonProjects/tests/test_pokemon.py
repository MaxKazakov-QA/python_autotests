import requests
import pytest
host = 'https://pokemonbattle.me:9104'
token = 'cb45216935ade887a2b3b82af663e60d'

def test_status_code():
    answer = requests.get(f'{host}/trainers', params={'trainer_id' : 4687})
    assert answer.status_code == 200