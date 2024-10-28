import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/goodbye')
def get_goodbye():
    return render_template('goodbye.html')

@app.route('/albums')
def get_albums():
    repo = AlbumRepository(get_flask_database_connection(app))
    albums = repo.all()
    return render_template("albums.html", albums=albums)

@app.route('/albums/<id>')
def get_specific_albums(id):
    albumrepo = AlbumRepository(get_flask_database_connection(app))
    artistrepo = ArtistRepository(get_flask_database_connection(app))
    album = albumrepo.select(id)
    return render_template("album_specific.html", album=album, artist=artistrepo.select(album[0]['artist_id'])[0]['name'])

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
