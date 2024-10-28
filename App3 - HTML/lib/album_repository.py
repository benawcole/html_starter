from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        records = self._connection.execute("SELECT * FROM albums")
        albums = []
        for record in records:
            album = Album(record["id"], record["title"], record["release_year"], record["artist_id"])
            albums.append(album)
        return albums

    def add(self, album):
        self._connection.execute("INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)", [f'{album.title}', album.release_year, album.artist_id])
        return None

    def select(self, id):
        return self._connection.execute("SELECT * FROM albums WHERE id = %s", [id])
        