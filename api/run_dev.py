"""Run the Flask development server with proper path setup."""
import sys, os

# Add repo root to path so 'api' package resolves correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ['FLASK_ENV'] = 'development'

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'), override=False)

from api.app_factory import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
