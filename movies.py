import requests


def get_movie_data(movie_name):
    url = "https://yts.mx/api/v2/list_movies.json"
    params = {
        "query_term": movie_name
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data


def get_movie_details(movie_data):

    movie_list = movie_data["data"]["movies"]
    # order by download count

    for movie in movie_list:
        print(f"Title: {movie['title']}")
        print(f"Year {movie['year']}")
        print(f"Summary: {movie['summary']}")
        for torrent in movie["torrents"]:
            if torrent["quality"] == "2160p" or torrent["quality"] == "1080p":
                print(f"Quality: {torrent['quality']}")
                print(f"Size: {torrent['size']}")
                print(f"Magnet link: {torrent['url']}")
                print('++++++++++++++++++++++++++++++++++++++++++++++++++++')

        print("========================================================")


def main():
    while True:
        movie_name = input("Ingresar nombre de la pelicula: ")

        movie_data = get_movie_data(movie_name)
        get_movie_details(movie_data)
        user_input = input("Quieres buscar nuevamente? (s/n): ").lower()
        while user_input not in ["s", "n"]:
            user_input = input("Quieres buscar nuevamente? (s/n): ").lower()
        if user_input == "n":
            break


if __name__ == "__main__":
    main()
