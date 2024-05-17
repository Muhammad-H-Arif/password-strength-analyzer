from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import re

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Load common passwords
common_passwords = set()
with open("app/common_passwords/passwords.txt", "r", encoding="utf-8") as file:
    for line in file:
        common_passwords.add(line.strip())

def calculate_entropy(password: str) -> float:
    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'\d', password):
        charset_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset_size += 32

    entropy = len(password) * (charset_size.bit_length())
    return entropy

@app.get("/")
async def get():
    return HTMLResponse(open("app/templates/index.html").read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            password = await websocket.receive_text()
            if password in common_passwords:
                feedback = "Weak password (common password)."
            else:
                entropy = calculate_entropy(password)
                if entropy < 50:
                    feedback = "Weak password."
                else:
                    feedback = "Strong password."
            await websocket.send_text(feedback)
        except WebSocketDisconnect:
            break
