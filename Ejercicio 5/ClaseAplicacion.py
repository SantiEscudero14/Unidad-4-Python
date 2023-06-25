import requests
import tkinter as tk
from tkinter import messagebox


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cinéfilos Argentinos")
        self.geometry("400x400")

        self.API_KEY = 'aquí_va_tu_api_key'

        self.BASE_URL = 'https://api.themoviedb.org/3/discover/movie'

        self.listbox = tk.Listbox(self)
        self.listbox.pack(pady=10)

        self.get_movies_button = tk.Button(self, text="Obtener películas", command=self.getPelicula)
        self.get_movies_button.pack(pady=10)

        self.listbox.bind("<Double-Button-1>", self.MostrarDetallesPelicula)

    def getPelicula(self):
        try:
            response = requests.get(self.BASE_URL, params={'api_key': self.API_KEY})
            response.raise_for_status()
            data = response.json()

            movies = data['results']

            self.listbox.delete(0, tk.END)

            for movie in movies:
                title = movie['title']
                self.listbox.insert(tk.END, title)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", str(e))

    def MostrarDetallesPelicula(self, event):
        selected_index = self.listbox.curselection()
        if len(selected_index) > 0:
            index = selected_index[0]

            try:
                response = requests.get(self.BASE_URL, params={'api_key': self.API_KEY})
                response.raise_for_status()
                data = response.json()

                movie = data['results'][index]
                titulo = movie['title']
                descripcion = movie['overview']
                lenguaje = movie['original_language']
                release_date = movie['release_date']
                genero = movie['genre_ids']

                genreNom = self.getGenerosNombre(genero)

                messagebox.showinfo("Detalles de la película",
                                    f"Título: {titulo}\n"
                                    f"Resumen: {descripcion}\n"
                                    f"Lenguaje original: {lenguaje}\n"
                                    f"Fecha de lanzamiento: {release_date}\n"
                                    f"Géneros: {', '.join(genreNom)}")
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", str(e))
    
    def getGenerosNombre(self, genre_ids):
        try:
            response = requests.get('https://api.themoviedb.org/3/genre/movie/list',
                                    params={'api_key': self.API_KEY})
            response.raise_for_status()
            data = response.json()

            genres = {genre['id']: genre['name'] for genre in data['genres']}

            genre_names = [genres[genre_id] for genre_id in genre_ids]

            return genre_names
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", str(e))

    def ejecutar(self):
        self.mainloop()
        

    
