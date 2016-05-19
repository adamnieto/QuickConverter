"""Helper to run the app"""
from os import getenv
from quick_lc3_convert import app
if __name__ == "__main__":
    port = getenv("PORT", 8000)
    app.run(host="0.0.0.0", port=port)
