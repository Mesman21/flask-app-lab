from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    from .users import users_bp
    from .products import products_bp
    from .posts import post_bp

    # --- ДОДАЄМО ЦІ ДВА РЯДКИ ---
    from .views import main_bp
    app.register_blueprint(main_bp)
    # ----------------------------

    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(post_bp)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app