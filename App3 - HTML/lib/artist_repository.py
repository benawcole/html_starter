from lib.artist import Artist

class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        records = self._connection.execute("SELECT * FROM artists")
        artists = []
        for record in records:
            artist = Artist(record["id"], record["name"], record["genre"])
            albums.append(artist)
        return artists

    def add(self, artist):
        self._connection.execute("INSERT INTO artist (name, genre) VALUES (%s, %s)", [f'{artist.name}', f'{artist.genre}'])
        return None

    def select(self, id):
        return self._connection.execute("SELECT * FROM artists WHERE id = %s", [id])