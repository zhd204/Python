from pprint import pprint
import os

import requests


class MovieSearch:
    movie_endpoint = "https://api.themoviedb.org/3/search/movie"
    movie_details_endpoint = "https://api.themoviedb.org/3/movie"
    configuration_endpoint = "https://api.themoviedb.org/3/configuration"

    def __init__(self):
        # bearer_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZTA3MTQ2OGI0YmY5NTRhYzk1MjVjNTNmZGU2MTE5NSIsInN1YiI6IjYyMjY1Mjc2MTEzODZjMDA3MjM4ZDIzMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.kncnGul59mOYn_KLFpi1jhzMktunzY5a9qG3IPkgmKc"
        bearer_token = os.environ.get("BEARER_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json;charset=utf-8"
        }

    def get_config(self):
        search_response = requests.get(url=self.configuration_endpoint, headers=self.headers)
        search_response.raise_for_status()
        configuration = search_response.json()
        secure_base_url = configuration["images"]["secure_base_url"]
        poster_sizes = configuration["images"]["poster_sizes"]
        return secure_base_url, poster_sizes

    def get_poster_url(self, poster_path, size_index):
        # poster_sizes array is ["w92", "w154", "w342", "w500", "w780", "original"]
        base_url, poster_sizes = self.get_config()
        poster_url = f"{base_url}{poster_sizes[size_index]}{poster_path}"
        return poster_url

    def get_results(self, keyword):
        """ Search for movies with keywords in the title """
        parameters = {
            "query": keyword
        }
        search_response = requests.get(url=self.movie_endpoint, params=parameters, headers=self.headers)
        search_response.raise_for_status()
        results = search_response.json()
        return results

    def get_details(self, movie_id):
        """ Search for movie details with movie id in the title """

        search_response = requests.get(url=f"{self.movie_details_endpoint}/{movie_id}", headers=self.headers)
        search_response.raise_for_status()
        details = search_response.json()
        return details
