#from . import create_app
from backend.app import create_app
from .database import engine
from .models import Base

app = create_app()

if __name__ == "__main__":

    print("Creating database tables...")
    with app.app_context():
        Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")
    
    app.run(debug=True)