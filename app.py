"""Helper to run the app"""
from os import getenv
from quick_lc3_converter import app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
