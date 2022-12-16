import requests
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Movie Search")
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

# Create a label and text box for the movie name
movie_label = tk.Label(root, text="Movie name:")
movie_name = tk.Entry(root)

# Create a function to be called when the search button is clicked
def search():
    # Get the movie name from the text box
    name = movie_name.get()

    # Call the get_movie_data function
    movie_data = get_movie_data(name)

    # Clear the results label
    results_label['text'] = ""

    # Iterate over the movie data and append the details to the results label
    movie_list = movie_data["data"]["movies"]
    for movie in movie_list:
        results_label['text'] += f"Title: {movie['title']}\n"
        results_label['text'] += f"Year {movie['year']}\n"
        results_label['text'] += f"Summary: {movie['summary']}\n"

        for torrent in movie["torrents"]:
            if torrent["quality"] == "2160p" or torrent["quality"] == "1080p":
                results_label['text'] += f"Quality: {torrent['quality']}\n"
                results_label['text'] += f"Size: {torrent['size']}\n"
                results_label['text'] += f"Magnet link: {torrent['url']}\n"
                results_label['text'] += '\n'

        results_label['text'] += "========================================================\n"

# Create a button to initiate the search
search_button = tk.Button(root, text="Search", command=search)

# Create a label to display the results
results_label = tk.Label(root, text="", wraplength=500)

# Use the grid layout manager to place the widgets
movie_label.grid(row=0, column=0)
movie_name.grid(row=0, column=1)
search_button.grid(row=0, column=2)
results_label.grid(row=1, column=0, columnspan=3)

# Start the main loop
root.mainloop()
