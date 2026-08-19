# Server README

This folder contains a prototype backend for AI Space (FastAPI + WebSocket + SQLite) with simple token-based auth.

Quick start (local):

1) Create virtualenv (optional) and install dependencies

   python -m venv .venv
   source .venv/bin/activate   # or .\venv\Scripts\activate on Windows
   pip install -r requirements.txt

2) Start server

   uvicorn server:app --host 0.0.0.0 --port 8001

3) Endpoints

- GET /api/ping
- POST /api/rooms  -> {"session": "ai-...", "token": "..."}
- POST /api/rooms/register_from_room  -> {"session": "ai-...", "token":"...", "url":"http://<host>/web/ai-space/index.html?session=..."}
- GET /api/rooms/{session}?token=...  or provide header Authorization: Bearer <token>
- POST /api/rooms/{session}  (body {state: {...}}) with token
- DELETE /api/rooms/{session} with token
- WebSocket /ws/{session}?token=...  -> receive/send JSON messages for realtime events

Notes
- When creating a room via register_from_room the server now returns a URL *without* the token embedded. The token is included in the JSON response but must be delivered to the room owner via a private channel. This prevents accidental public sharing of the token.
