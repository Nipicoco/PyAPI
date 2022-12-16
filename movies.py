import requests


def get_movie_data(movie_name):
    url = "https://yts.mx/api/v2/list_movies.json"
    params = {
        "query_term": movie_name,
        'sort_by': 'download_count',
        'limit': 5,
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data


def get_movie_details(movie_data):
    movie_list = movie_data["data"]["movies"]
    for movie in movie_list:
        print(f"Title: {movie['title']}")
        print(f"Year {movie['year']}")
        print(f"Summary: {movie['summary']}")

        for torrent in movie["torrents"]:
            if torrent["quality"] == "2160p" or torrent["quality"] == "1080p":
                print(f"Quality: {torrent['quality']}")
                print(f"Size: {torrent['size']}")
                print(f"Magnet link: {torrent['url']}")
                print('\n')

        print("========================================================")


def save_movie_data(movie_data):
    movie_list = movie_data["data"]["movies"]

    with open("movies.txt", "a") as file:

        for movie in movie_list:
            file.write(f"Title: {movie['title']}\n")
            file.write(f"Year {movie['year']}\n")
            file.write(f"Rating: {movie['rating']}\n")

            for torrent in movie["torrents"]:
                if torrent["quality"] == "2160p" or torrent["quality"] == "1080p":
                    file.write(f"Quality: {torrent['quality']}\n")
                    file.write(f"Size: {torrent['size']}\n")
                    file.write(f"Magnet link: {torrent['url']}\n")
                    file.write("")

            file.write(
                "========================================================\n")

        file.close()


def main():
    while True:
        movie_name = input("Ingresar nombre de la pelicula: ")

        movie_data = get_movie_data(movie_name)
        get_movie_details(movie_data)
        save = input("Quieres guardar los datos? (s/n): ").lower()
        while save not in ["s", "n"]:
            save = input("Quieres guardar los datos? (s/n): ").lower()
        if save == "s":
            save_movie_data(movie_data)
        else:
            print("No se guardaron los datos")

        user_input = input("Quieres buscar nuevamente? (s/n): ").lower()
        while user_input not in ["s", "n"]:
            user_input = input("Quieres buscar nuevamente? (s/n): ").lower()
        if user_input == "n":
            break


if __name__ == "__main__":
    main()
