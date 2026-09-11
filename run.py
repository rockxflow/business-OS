"""Rockxflow OS - entry point. Run: python run.py"""
import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    # 0.0.0.0 so live preview + LAN access works. Debug off for safety.
    app.run(host="0.0.0.0", port=port, debug=False)
