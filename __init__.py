from flask import Flask 

def create_app():
    app = Flask(__name__)

    
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app