# 🎤 Clubhouse Invite Bot

Automatically send invites and welcome messages to users in Clubhouse rooms!

## ✨ Features

- 🎯 Auto-send invites to multiple users
- 💬 Send custom welcome messages
- 📊 CSV-based user list management
- ⏰ Scheduled message sending
- 📝 Detailed logging system
- 🔧 Easy configuration
- 🛡️ Error handling & retries
- 🧪 Dry-run mode for testing

## 📋 Requirements

- Python 3.7+
- Windows/Mac/Linux
- Internet connection
- Clubhouse API credentials

## 🚀 Installation

### 1. Clone Repository
```bash
git clone https://github.com/Smokeexxxx/clubhouse-invite-bot-0.1.git
cd clubhouse-invite-bot-0.1
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Bot
Edit `config.py` with your Clubhouse credentials:
```python
CLUBHOUSE_API_KEY = "your_api_key"
CLUBHOUSE_API_SECRET = "your_api_secret"
CLUBHOUSE_USER_ID = "your_user_id"
TARGET_ROOM_ID = "your_room_id"
```

### 4. Add User List
Edit `users.csv` and add user IDs (one per line):
```
user_id_1
user_id_2
user_id_3
```

### 5. Run Bot
```bash
python main.py
```

## 📁 File Structure

```
clubhouse-invite-bot-0.1/
├── main.py              # Main bot application
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── users.csv           # User IDs list
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── bot.log             # Bot logs (auto-created)
```

## ⚙️ Configuration

### Basic Settings
- `CLUBHOUSE_API_KEY` - Your Clubhouse API key
- `CLUBHOUSE_API_SECRET` - Your Clubhouse API secret
- `CLUBHOUSE_USER_ID` - Your Clubhouse user ID
- `TARGET_ROOM_ID` - Target room ID for invites

### Automation Settings
- `CHECK_INTERVAL` - How often to check for new users (seconds)
- `MESSAGE_DELAY` - Delay between sending messages
- `AUTO_START` - Auto-start bot on launch

### Messages
- `INVITE_MESSAGE` - Custom invite message template
- `WELCOME_MESSAGE` - Welcome message for room members

### Advanced
- `DEBUG` - Enable debug logging
- `DRY_RUN` - Test without sending real messages
- `MAX_RETRIES` - Maximum API retry attempts
- `TIMEOUT` - API request timeout

## 📖 Usage

### Normal Mode
```bash
python main.py
```

### Debug Mode
Edit `config.py`:
```python
DEBUG = True
```

### Test Mode (Dry Run)
Edit `config.py`:
```python
DRY_RUN = True
```

## 📊 Logging

Bot logs are saved to `bot.log` with timestamps and detailed information:
- ✅ Successful invites
- ❌ Failed attempts
- ⏳ API rate limiting
- 🔍 Debug information

View logs:
```bash
type bot.log
```

## 🐛 Troubleshooting

### Error: "API credentials invalid"
- Check `config.py` for correct API key and secret
- Verify credentials are in quotes

### Error: "users.csv not found"
- Make sure `users.csv` exists in the same folder
- Check file name spelling

### Error: "Rate limit exceeded"
- Increase `MESSAGE_DELAY` in config.py
- Reduce number of users to invite at once

### Bot not sending messages
- Enable `DEBUG = True` in config.py
- Check `bot.log` for error messages
- Test with `DRY_RUN = True` first

## 🔐 Security

- Never commit API credentials to git
- Use `.gitignore` to exclude sensitive files
- Consider using environment variables for production
- Keep your API keys private

## 📦 Building EXE (Windows)

Convert to standalone executable:

```bash
pyinstaller --onefile --windowed main.py
```

EXE will be in `dist/` folder

## 📝 License

MIT License - Feel free to use and modify!

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📧 Support

For issues and questions:
- Check `bot.log` for error details
- Review configuration in `config.py`
- Enable `DEBUG = True` for more information

## ⭐ Features Coming Soon

- [ ] Web dashboard
- [ ] Database support
- [ ] Advanced filtering
- [ ] Multi-room support
- [ ] Webhook integration

---

**Made with ❤️ by Smokeexxxx**

🚀 Happy inviting!