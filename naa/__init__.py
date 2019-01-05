import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('home.html', layout = "home")

    @app.route('/about')
    def about():
        return render_template('about.html', layout = "about")

    @app.route('/gallery')
    def get_gallery_content():
    gallery_image_names = os.listdir('./static/images/gallery')
        return render_template("gallery.html", layout = "gallery", gallery_image_names=gallery_image_names)

    @app.route('/bio')
    def get_bio():
    bio_image_names = os.listdir('./static/images/bio')
        return render_template("bio.html", layout = "bio", bio_image_names=bio_image_names)

    @app.route('/merch')
    def get_merch():
    merch_image_names = os.listdir('./static/images/merch')
        return render_template("merch.html", layout = "merch", merch_image_names=merch_image_names)

    return app