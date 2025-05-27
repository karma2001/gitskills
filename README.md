# Bitcoin Transaction Demo

This repository contains a small example showing how to send Bitcoin using a
FastAPI backend connected to a Bitcoin Core node and a minimal HTML frontend.

## Running the backend

Edit `backend/main.py` and update the `BITCOIN_RPC_*` constants so they match
your local Bitcoin Core configuration. Then start the server with:

```bash
uvicorn backend.main:app --reload
```

The backend exposes two endpoints under the `/api` prefix:

- `GET /api/balance/{address}` – returns the balance for a specific address.
- `POST /api/send` – sends bitcoin to the given address using `sendtoaddress`.

## Using the frontend

Open `frontend/index.html` in your browser. It provides a simple form to send
bitcoin by issuing requests to the backend API.
