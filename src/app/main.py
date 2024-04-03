from flask import Flask
from views import init_views

# flask --app ./src/app/main.py run --debug -p 5000

def create_app():
    app = Flask(
        __name__,
        template_folder="../ui/templates", 
        static_folder="../ui/static"
    )
    init_views(app)
    
    return app
