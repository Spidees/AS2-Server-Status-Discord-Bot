# Steam A2S Discord Bot

A minimalistic Discord bot that uses the **Steam A2S (Source Engine Query)** protocol to monitor any game server that supports it – such as **V Rising**, **Valheim**, **Rust**, **CS:GO**, **7 Days to Die**, and more.

It displays server name, current players, and status in both Discord embeds and the bot's presence.

---

## ✅ Games that Support Steam A2S (Query Protocol)

### 🎮 Source / GoldSrc Engine Games
| Game                      | A2S Support | Notes                  |
|---------------------------|-------------|-------------------------|
| Counter-Strike 1.6        | ✅           | Classic GoldSrc        |
| CS:GO / CS2               | ✅           | Fully supported         |
| Team Fortress 2           | ✅           |                        |
| Day of Defeat: Source     | ✅           |                        |
| Left 4 Dead 1 & 2         | ✅           |                        |
| Garry's Mod               | ✅           | Popular and compatible |
| Half-Life 1 & 2 / Deathmatch | ✅        |                        |
| Sven Co-op                | ✅           | HL1-based               |

### 🧪 Survival / Multiplayer Games
| Game                      | A2S Support | Notes                        |
|---------------------------|-------------|-------------------------------|
| V Rising                  | ✅           | Tested and works             |
| Valheim                   | ✅           | Requires correct port         |
| Rust                      | ✅           | Full support                  |
| 7 Days to Die             | ✅           | Needs A2S port                |
| ARK: Survival Evolved     | ✅           | Use query port                |
| Conan Exiles              | ✅           | Query port needed             |
| Unturned                  | ✅           | Full support                  |
| Killing Floor 2           | ✅           | Steam query compatible        |

### ⚠️ Partial or No A2S Support
| Game                      | A2S Support | Notes                                  |
|---------------------------|-------------|-----------------------------------------|
| Minecraft (vanilla)       | ❌           | Uses its own query protocol             |
| FiveM (GTA V)             | ❌           | Has its own custom API                  |
| Factorio                  | ❌           | Offers HTTP API, not A2S                |
| SCP: Secret Laboratory    | ⚠️           | Custom query, may vary by version       |
| Terraria                  | ⚠️           | Depends on server setup                 |

---

## ✅ Features

### 📊 Server Status to Discord
- Queries the game server using the A2S protocol
- Retrieves:
  - Server name
  - Player count / max players
- Sends or updates an embed message in a selected Discord channel
- Automatically refreshes every 60 seconds

### 🟢 Discord Presence Update
- Sets the bot's Discord status based on player count
- Format: `"X / Y players"` or `"Server offline"`

### 🔁 Offline Detection
- If the query fails, shows an offline embed with a red error message

---

## ⚙️ Environment Setup (`.env`)

```ini
DISCORD_TOKEN=your-discord-bot-token
SERVER_IP=your-server-ip
SERVER_PORT=your-query-port
CHANNEL_ID=your-discord-channel-id
```

---

## ▶️ Running

Install dependencies:

```bash
pip install -r requirements.txt
```

Then start the bot:

```bash
python bot.py
```

The bot will log in, post server status in the designated channel, and update it every minute.

---

## 🧩 Dependencies

- `discord.py`
- `python-dotenv`

Install them via:

```bash
pip install discord.py python-dotenv
```

Or use the provided `requirements.txt`.

---

## 📁 Project Structure

- `bot.py` – Main bot script  
- `.env` – Your environment configuration  
- `requirements.txt` – List of dependencies  

---

## 🔧 Tips & Notes

- Make sure your firewall allows traffic on the **query port**, not just the game port.  
- Most survival games use a different A2S port than the visible one in Steam.  
- You can run multiple bots (e.g. for multiple servers) by duplicating the project and changing `.env`.

---

## 💬 Community & Contact

Got questions, ideas, or want to show off your setup?  
Join the community here:

[![Discord Badge](https://img.shields.io/badge/Join%20us%20on-Discord-5865F2?style=flat&logo=discord&logoColor=white)](https://playhub.cz/discord)

---

## 🙌 Support

If you enjoy this project, consider supporting:

[![Ko-fi Badge](https://img.shields.io/badge/Support%20me%20on-Ko--fi-ff5e5b?style=flat&logo=ko-fi&logoColor=white)](https://ko-fi.com/playhub)  
[![PayPal Badge](https://img.shields.io/badge/Donate-PayPal-0070ba?style=flat&logo=paypal&logoColor=white)](https://paypal.me/spidees)

Thank you! ❤️
