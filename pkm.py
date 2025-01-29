import requests

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None

def calculate_stat(base_stat):
    return base_stat  # Placeholder function

def calculate_hp(base_stat):
    return base_stat  # Placeholder function

def extract_stats(pokemon_data):
    stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
    return {
        'attack': calculate_stat(stats['attack']),
        'defense': calculate_stat(stats['defense']),
        'speed': calculate_stat(stats['speed']),
        'hp': calculate_hp(stats['hp'])
    }

def battle(pokemon1_name, pokemon2_name):
    pokemon1_data = get_pokemon_data(pokemon1_name)
    pokemon2_data = get_pokemon_data(pokemon2_name)
    
    if not pokemon1_data or not pokemon2_data:
        return
    
    stats1 = extract_stats(pokemon1_data)
    stats2 = extract_stats(pokemon2_data)
    
    print(f"Battle Start: {pokemon1_name.capitalize()} vs {pokemon2_name.capitalize()}")
    print(f"{pokemon1_name.capitalize()} HP: {stats1['hp']}")
    print(f"{pokemon2_name.capitalize()} HP: {stats2['hp']}")
    
    if stats1['speed'] > stats2['speed']:
        attacker_name, defender_name = pokemon1_name, pokemon2_name
        attacker_stats, defender_stats = stats1, stats2
    else:
        attacker_name, defender_name = pokemon2_name, pokemon1_name
        attacker_stats, defender_stats = stats2, stats1
    
    round_num = 1
    while attacker_stats['hp'] > 0 and defender_stats['hp'] > 0:
        print(f"Round {round_num}")
        damage = attacker_stats['attack'] - defender_stats['defense']
        damage = max(damage, 1)  # Ensure at least 1 damage
        defender_stats['hp'] -= damage
        print(f"{attacker_name.capitalize()} deals {damage} damage to {defender_name.capitalize()}")
        print(f"{defender_name.capitalize()} HP: {max(defender_stats['hp'], 0)}")
        
        if defender_stats['hp'] <= 0:
            print(f"{defender_name.capitalize()} fainted! {attacker_name.capitalize()} wins!")
            break
        
        attacker_name, defender_name = defender_name, attacker_name
        attacker_stats, defender_stats = defender_stats, attacker_stats
        round_num += 1

battle("Charmander","Squirtle")