'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Pikachu")
    print(poke_info)
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    removed_space_pokeon_nm = pokemon_name.strip()
    clean_pokemonnm = removed_space_pokeon_nm.lower()
    # TODO: Build a clean URL and use it to send a GET request
    request_url =  f'https://pokeapi.co/api/v2/pokemon/{clean_pokemonnm}'
    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    resp_msg = requests.get(request_url)
    body_dict = resp_msg.json()
    # TODO: If the GET request failed, print the error reason and return None
    if resp_msg.status_code == requests.codes.ok:
        print(f"Getting information for {clean_pokemonnm}...success")
        return body_dict
    else:
        print(f"Getting information for {clean_pokemonnm}...failure")
        print(f'Response code: { resp_msg.status_code } ({resp_msg.reason})')
        return None
    

if __name__ == '__main__':
    main()