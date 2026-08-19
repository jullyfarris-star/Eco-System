const express = require('express');
const cors = require('cors');
const fs = require('fs').promises;
const path = require('path');

const app = express();
app.use(cors());
app.use(express.json());

const DATA_DIR = path.join(__dirname, 'data');
const DATA_FILE = path.join(DATA_DIR, 'rooms.json');

async function ensureDataFile() {
  try {
    await fs.mkdir(DATA_DIR, { recursive: true });
    await fs.access(DATA_FILE);
  } catch (e) {
    await fs.writeFile(DATA_FILE, JSON.stringify({}), 'utf8');
  }
}

async function readRooms() {
  await ensureDataFile();
  const text = await fs.readFile(DATA_FILE, 'utf8');
  try {
    return JSON.parse(text || '{}');
  } catch (e) {
    return {};
  }
}

async function writeRooms(obj) {
  await ensureDataFile();
  await fs.writeFile(DATA_FILE, JSON.stringify(obj, null, 2), 'utf8');
}

function generateSessionId() {
  return 'ai-' + Date.now().toString(36) + '-' + Math.random().toString(36).substr(2, 6);
}

// Healthcheck
app.get('/api/ping', (req, res) => {
  res.json({ ok: true });
});

// Create new room
app.post('/api/rooms', async (req, res) => {
  const rooms = await readRooms();
  const session = generateSessionId();
  const initial = req.body && req.body.initial ? req.body.initial : { objects: [] };
  rooms[session] = { created: Date.now(), updated: Date.now(), state: initial };
  await writeRooms(rooms);
  res.json({ session, state: rooms[session].state });
});

// Get room state
app.get('/api/rooms/:session', async (req, res) => {
  const session = req.params.session;
  const rooms = await readRooms();
  if (!rooms[session]) return res.status(404).json({ error: 'not_found' });
  return res.json({ session, state: rooms[session].state });
});

// Update room state (replace)
app.post('/api/rooms/:session', async (req, res) => {
  const session = req.params.session;
  const state = req.body || { objects: [] };
  const rooms = await readRooms();
  rooms[session] = rooms[session] || { created: Date.now() };
  rooms[session].state = state;
  rooms[session].updated = Date.now();
  await writeRooms(rooms);
  return res.json({ session, state: rooms[session].state });
});

// Delete room
app.delete('/api/rooms/:session', async (req, res) => {
  const session = req.params.session;
  const rooms = await readRooms();
  if (!rooms[session]) return res.status(404).json({ error: 'not_found' });
  delete rooms[session];
  await writeRooms(rooms);
  return res.json({ ok: true });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`AI Space server listening on http://localhost:${PORT}`);
});
