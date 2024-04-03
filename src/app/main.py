from flask import Flask


def init_app():
    app = Flask(
        __name__,
        template_folder="../ui/templates", 
        static_folder="../ui/static"
    )
    
    return app
