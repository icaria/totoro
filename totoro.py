import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    keys = {
        "mapbox_access_token" : "pk.eyJ1IjoiaWNhcmlhIiwiYSI6ImNpZjczc3I5cTAyb2dyeWx6Z2Mzanlld3cifQ.jBkG4gWBX37zKjrbkX7SRg",
        "mapbox_map_id": "icaria.cif73spzl02orshlz4eep3nfq",
        "foursquare_client_id": "IUEZ42RZ5SAY4J0E0TOHB34R15GW2RRV2OQUQNXQIKYONHPN",
        "foursquare_authentication_url": "https://foursquare.com/",
        "foursquare_api_url":"https://api.foursquare.com/"
    }
    return render_template('index.html', name="Stephen Chen", title="Software Engineer", keys=keys)


if __name__ == '__main__':
    app.run()
