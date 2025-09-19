import requests
from langchain.tools import tool
from config.settings import JSONTOJAVA_SERVICE

@tool
def get_all_movies() -> str:
    """
    Fetch all movies.
    """
    try:
        response = requests.get(f"{JSONTOJAVA_SERVICE}")
        response.raise_for_status()
        movies = response.json()
        return f"All movies: {movies}"
    except requests.RequestException as e:
        return f"Error fetching movies: {str(e)}"

@tool
def get_titles() -> str:
    """
    Fetch all trackName and collectionName pairs.
    """
    try:
        response = requests.get(f"{JSONTOJAVA_SERVICE}/titles")
        response.raise_for_status()
        titles = response.json()
        return f"Titles: {titles}"
    except requests.RequestException as e:
        return f"Error fetching titles: {str(e)}"

@tool
def get_movie_by_track_id(track_id: int) -> str:
    """
    Fetch a movie by its track ID.
    """
    try:
        response = requests.get(f"{JSONTOJAVA_SERVICE}/{track_id}")
        if response.status_code == 404:
            return f"No movie found with track ID {track_id}."
        response.raise_for_status()
        movie = response.json()
        return f"Movie: {movie}"
    except requests.RequestException as e:
        return f"Error fetching movie by track ID {track_id}: {str(e)}"

@tool
def get_movies_by_price_less_than(max_price: float) -> str:
    """
    Fetch movies with collectionPrice less than the given max price.
    """
    try:
        response = requests.get(f"{JSONTOJAVA_SERVICE}/filter/price", params={"max": max_price})
        response.raise_for_status()
        movies = response.json()
        return f"Movies with price less than {max_price}: {movies}"
    except requests.RequestException as e:
        return f"Error fetching movies by price less than {max_price}: {str(e)}"
    

json_to_java_tools = [get_all_movies, get_titles, get_movie_by_track_id, get_movies_by_price_less_than]