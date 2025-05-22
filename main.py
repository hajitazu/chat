from fastapi import FastAPI, WebSocket, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import status

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

active_connections = {}

def is_valid_user_id(user_id: str) -> bool:
    if not user_id.isdigit():
        return False
    num = int(user_id)
    return 1 <= num <= 300

@app.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

@app.post("/chat", response_class=HTMLResponse)
async def chat_page(request: Request, user_id: str = Form(...)):
    if not is_valid_user_id(user_id):
        return templates.TemplateResponse("login.html", {"request": request, "error": "ID harus angka antara 1 sampai 300"})
    return templates.TemplateResponse("chat.html", {"request": request, "user_id": user_id})

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    if not is_valid_user_id(user_id):
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    await websocket.accept()
    active_connections[user_id] = websocket
    try:
        while True:
            data = await websocket.receive_json()
            to_id = data.get("to")
            message = data.get("message")
            if to_id in active_connections:
                await active_connections[to_id].send_json({"from": user_id, "message": message})
    except:
        active_connections.pop(user_id, None)
