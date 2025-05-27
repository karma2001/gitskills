from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path
import json
import base64
import urllib.request

# Configuration for Bitcoin Core RPC
BITCOIN_RPC_URL = "http://localhost:8332/"
BITCOIN_RPC_USER = "user"
BITCOIN_RPC_PASSWORD = "password"

app = FastAPI()

# Serve the frontend static files
frontend_path = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

class TransactionRequest(BaseModel):
    to_address: str
    amount: float


def call_rpc(method: str, params=None):
    if params is None:
        params = []
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 0,
        "method": method,
        "params": params
    }).encode()

    req = urllib.request.Request(BITCOIN_RPC_URL, data=payload)
    credentials = f"{BITCOIN_RPC_USER}:{BITCOIN_RPC_PASSWORD}"
    req.add_header("Authorization", "Basic " + base64.b64encode(credentials.encode()).decode())
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read())


@app.get("/api/balance/{address}")
def get_balance(address: str):
    """Return the balance for a given address."""
    return call_rpc("getreceivedbyaddress", [address])


@app.post("/api/send")
def send_transaction(tx: TransactionRequest):
    """Send bitcoin to the specified address."""
    return call_rpc("sendtoaddress", [tx.to_address, tx.amount])
