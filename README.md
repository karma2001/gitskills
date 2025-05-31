# Data Exchange Sharing Platform

This repository contains a simple data exchange platform. It has a minimal
backend written with Node's built-in modules and a frontend built with plain
HTML, CSS and JavaScript.

## Running

Run the server with:

```bash
node server.js
```

The application will be available at `http://localhost:3000`.

## Project Structure

- `server.js` - simple HTTP server that exposes `/api/data` and serves files in
  `public`.
- `data/data.json` - sample JSON data returned by the API.
- `public/` - frontend files (HTML/CSS/JS).

