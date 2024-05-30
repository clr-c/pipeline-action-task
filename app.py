echo from flask import Flask > app.py
echo. >> app.py
echo app = Flask(__name__) >> app.py
echo. >> app.py
echo @app.route('/') >> app.py
echo def hello_world(): >> app.py
echo     return 'Hello, World!' >> app.py
echo. >> app.py
echo if __name__ == '__main__': >> app.py
echo     app.run(debug=True) >> app.py