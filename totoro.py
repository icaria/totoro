import os
import foursquare
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)

foursquare_access_token = os.environ.get('foursquare_access_token')
mapbox_access_token = os.environ.get('mapbox_access_token')
foursquare_redirect_uri = os.environ.get('foursquare_redirect_uri')


@app.route('/')
def index():
    if foursquare_access_token is not None:
        foursquare_client = foursquare.Foursquare(access_token=foursquare_access_token,
                                                  redirect_uri=foursquare_redirect_uri)

        last_check_in = foursquare_client.users.checkins(params={'limit': 1})['checkins']['items'][0]
        venue = last_check_in['venue']
        latitude = venue['location']['lat']
        longitude = venue['location']['lng']

        keys = {
            "mapbox_access_token" : mapbox_access_token,
            "venue": venue['name'],
            "lat": latitude,
            "lng": longitude
        }

        return render_template('index.html', name="Stephen Chen", title="Software Development Engineer", keys=keys)


if __name__ == '__main__':
    app.run()
