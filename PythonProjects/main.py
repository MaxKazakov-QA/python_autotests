import requests

host = 'https://pokemonbattle.me:9104'
token = 'cb45216935ade887a2b3b82af663e60d'


answer_create_pokemon = requests.post(f'{host}/pokemons', json={
    "name": "Autopikachu",
    "photo": "https://dolnikov.ru/pokemons/albums/025.png"
}, headers={"trainer_token" : token, "Content-Type" : "application/json"} )

print(answer_create_pokemon.text)

answer_rename_pokemon = requests.put(f'{host}/pokemons', json={
    "pokemon_id": "13260",
    "name": "NewAutoPoke",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers={"trainer_token" : token, "Content-Type" : "application/json"})
print(answer_rename_pokemon.text)



answer_catch_pokemon = requests.post(f'{host}/trainers/add_pokeball', json={
    "pokemon_id": "13260"
}, headers={"trainer_token" : token, "Content-Type" : "application/json"})
print(answer_catch_pokemon.text)