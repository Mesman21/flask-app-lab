import os
from app import create_app

config_name = os.getenv('FLASK_CONFIG') or 'default'
app = create_app(config_name)

if __name__ == "__main__":

    print("Link: http://127.0.0.1:5000/")

    app.run(debug=True)