import os
import foursquare
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config.from_object(__name__)

foursquare_client_id = os.environ.get('foursquare_client_id')
foursquare_client_secret = os.environ.get('foursquare_client_secret')
foursquare_redirect_uri = os.environ.get('foursquare_redirect_uri')


@app.route('/')
def index():
    foursquare_access_token = os.environ.get('foursquare_access_token')

    if foursquare_access_token is not None:
        foursquare_client = foursquare.Foursquare(access_token=foursquare_access_token,
                                                  redirect_uri=foursquare_redirect_uri)
    else:
        foursquare_client = foursquare.Foursquare(client_id=foursquare_client_id,
                                                  client_secret=foursquare_client_secret,
                                                  redirect_uri=foursquare_redirect_uri)

        auth_url = foursquare_client.oauth.auth_url()

        return redirect(auth_url)

    last_check_in = foursquare_client.users.checkins(params={'limit': 1})['checkins']['items'][0]
    venue = last_check_in['venue']
    latitude = venue['location']['lat']
    longitude = venue['location']['lng']

    keys = {
        "mapbox_access_token" : "pk.eyJ1IjoiaWNhcmlhIiwiYSI6ImNpZjczc3I5cTAyb2dyeWx6Z2Mzanlld3cifQ.jBkG4gWBX37zKjrbkX7SRg",
        "venue": venue['name'],
        "lat": latitude,
        "lng": longitude
    }

    return render_template('index.html', name="Stephen Chen", title="Software Development Engineer", keys=keys)


@app.route('/callback')
def auth():
    foursquare_authorization_code = request.args.get('code').encode('ascii', 'ignore')
    foursquare_client = foursquare.Foursquare(client_id=foursquare_client_id,
                                              client_secret=foursquare_client_secret,
                                              redirect_uri=foursquare_redirect_uri)

    foursquare_access_token = foursquare_client.oauth.get_token(foursquare_authorization_code)

    os.environ['foursquare_access_token'] = foursquare_access_token
    return redirect('/')


if __name__ == '__main__':
    app.run()
