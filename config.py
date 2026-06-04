"""
Configuration file for Clubhouse Invite Bot
Edit these settings before running the bot
"""

# ============================================
# CLUBHOUSE API CREDENTIALS
# ============================================
CLUBHOUSE_API_KEY = "your_api_key_here"
CLUBHOUSE_API_SECRET = "your_api_secret_here"
CLUBHOUSE_USER_ID = "your_user_id_here"

# ============================================
# ROOM & CHANNEL SETTINGS
# ============================================
TARGET_ROOM_ID = "your_room_id_here"
TARGET_CHANNEL_ID = "your_channel_id_here"  # Optional

# ============================================
# AUTOMATION SETTINGS
# ============================================
CHECK_INTERVAL = 30  # Check for new users every X seconds
MESSAGE_DELAY = 2    # Delay between sending messages (seconds)
AUTO_START = True    # Auto-start bot on launch

# ============================================
# INVITE MESSAGE TEMPLATE
# ============================================
INVITE_MESSAGE = """
🎤 Hey there! 

You're invited to join our exclusive Clubhouse room!

Come chat with us about amazing topics. See you there! 🎉

#Clubhouse #Community
"""

# ============================================
# WELCOME MESSAGE TEMPLATE
# ============================================
WELCOME_MESSAGE = """
👋 Welcome to the room! 

We're excited to have you here! Feel free to:
- Listen to the discussion
- Raise your hand to speak
- Connect with other members

Enjoy! 🎵
"""

# ============================================
# USER LIST SETTINGS
# ============================================
# Option 1: Use CSV file
USE_CSV_FILE = True
CSV_FILE_PATH = "users.csv"  # File with user IDs (one per line)

# Option 2: Direct user list (if not using CSV)
USER_IDS_LIST = [
    # "user_id_1",
    # "user_id_2",
    # "user_id_3",
]

# ============================================
# LOGGING SETTINGS
# ============================================
LOG_FILE = "bot.log"
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
ENABLE_CONSOLE_LOG = True

# ============================================
# ADVANCED SETTINGS
# ============================================
TIMEOUT = 10  # API request timeout (seconds)
MAX_RETRIES = 3  # Retry failed requests
RATE_LIMIT_DELAY = 1  # Delay for API rate limiting (seconds)

# ============================================
# DEBUG MODE
# ============================================
DEBUG = False  # Set to True for verbose logging
DRY_RUN = False  # Set to True to test without sending real messages