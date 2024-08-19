import requests

def joke_generator(_):
    """
    Fetch a random joke from the official joke API.

    Parameters:
    _ (str): Placeholder parameter, not used.

    Returns:
    str: The fetched joke in the format "setup - punchline".
    """
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        response.raise_for_status()
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    except requests.RequestException as e:
        return f"Error fetching joke: {str(e)}"