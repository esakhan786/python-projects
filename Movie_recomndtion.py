import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import io
import webbrowser

API_KEY = "b41f9aee593080c1c5bcf348c404e418"

# Open TMDb movie page
def open_link(url):
    webbrowser.open(url)

# Fetch recommendations
def get_recommendations():
    movie_name = movie_entry.get().strip()
    if not movie_name:
        return

    # Clear previous recommendations
    for widget in results_frame.winfo_children():
        widget.destroy()

    # Search movie
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    search_resp = requests.get(search_url).json()
    if not search_resp['results']:
        tk.messagebox.showinfo("Not Found", f"No movie found with name '{movie_name}'")
        return

    movie_id = search_resp['results'][0]['id']

    # Get recommendations
    rec_url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={API_KEY}"
    rec_resp = requests.get(rec_url).json()

    if not rec_resp['results']:
        tk.messagebox.showinfo("No Recommendations", "No recommendations found.")
        return

    for rec in rec_resp['results'][:5]:
        # Movie details
        title = rec['title']
        rating = rec.get('vote_average', 'N/A')
        overview = rec.get('overview', 'No description available.')
        movie_link = f"https://www.themoviedb.org/movie/{rec['id']}"
        poster_path = rec.get('poster_path')

        # Frame for each movie
        frame = tk.Frame(results_frame, bd=1, relief=tk.RIDGE, padx=5, pady=5)
        frame.pack(fill='x', pady=5)

        # Poster Image
        if poster_path:
            img_url = f"https://image.tmdb.org/t/p/w200{poster_path}"
            response = requests.get(img_url)
            image_data = response.content
            img = Image.open(io.BytesIO(image_data))
            img = img.resize((100, 150))
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(frame, image=photo)
            img_label.image = photo
            img_label.pack(side='left', padx=5)

        # Movie Info
        info_frame = tk.Frame(frame)
        info_frame.pack(side='left', fill='x', expand=True)

        title_label = tk.Label(info_frame, text=f"{title} | Rating: {rating}", font=("Arial", 12, "bold"), fg="blue", cursor="hand2")
        title_label.pack(anchor='w')
        title_label.bind("<Button-1>", lambda e, url=movie_link: open_link(url))

        overview_label = tk.Label(info_frame, text=overview, wraplength=400, justify='left')
        overview_label.pack(anchor='w')

# GUI setup
root = tk.Tk()
root.title("Movie Recommender")
root.geometry("600x600")

tk.Label(root, text="Enter movie you watched:", font=("Arial", 12)).pack(pady=10)
movie_entry = tk.Entry(root, width=40, font=("Arial", 12))
movie_entry.pack(pady=5)

tk.Button(root, text="Get Recommendations", command=get_recommendations, font=("Arial", 12)).pack(pady=10)

# Scrollable results frame
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

results_frame = scrollable_frame

root.mainloop()