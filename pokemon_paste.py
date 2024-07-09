""" 
Description: 
  Creates a new PasteBin paste that contains a list of abilities 
  for a specified Pokemon

Usage:
  python pokemon_paste.py poke_name

Parameters:
  poke_name = Pokemon name
"""
import sys
import poke_api
import pastebin_api

def main():
    poke_name = get_pokemon_name()
    poke_info = poke_api.get_pokemon_info(poke_name)
    if poke_info is not None:
        paste_title, paste_body = get_paste_data(poke_info)
        paste_url = pastebin_api.post_new_paste(paste_title, paste_body, '1M')
        print(paste_url)

def get_pokemon_name():
    """Gets the name of the Pokemon specified as a command line parameter.
    Aborts script execution if no command line parameter was provided.

    Returns:
        str: Pokemon name
    """
    # TODO: Function body
    # Check if a command line parameter is provided
    if len(sys.argv) < 2:
        print("Error: No Pokemon name provided.")
        sys.exit(1)

    # Retrieve the Pokemon name from the command line arguments
    pokenm = sys.argv[1].strip()

    # Ensure the Pokemon name is not empty
    if not pokenm:
        print("Error: Provided Pokemon name is empty.")
        sys.exit(1)

    return pokenm

    

def get_paste_data(pokemon_info):
    """Builds the title and body text for a PasteBin paste that lists a Pokemon's abilities.

    Args:
        pokemon_info (dict): Dictionary of Pokemon information

    Returns:
        (str, str): Title and body text for the PasteBin paste
    """    
    # TODO: Build the paste title
    # TODO: Build the paste body text
    if not pokemon_info or 'abilities' not in pokemon_info:
        return None, None

    # Extract the Pokemon name and capitalize it
    pokenm = pokemon_info["forms"][0]["name"].capitalize()

    # Construct the paste title
    poke_title = f"{pokenm}'s Abilities"

    # Build the paste body text with formatted abilities
    body_withouttitle = [f"- {ability['ability']['name']}" for ability in pokemon_info["abilities"]]
    body = "\n".join(body_withouttitle)

    return poke_title, body


if __name__ == '__main__':
    main()