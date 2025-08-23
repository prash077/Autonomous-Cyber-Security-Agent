# in backend/app/main.py
from . import create_app
from .database import init_db

app = create_app()

if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)