"""
Clubhouse Invite Bot - Main Application
Auto-sends invites and welcome messages to users in Clubhouse
"""

import requests
import logging
import time
import csv
from datetime import datetime
from config import (
    CLUBHOUSE_API_KEY,
    CLUBHOUSE_API_SECRET,
    CLUBHOUSE_USER_ID,
    TARGET_ROOM_ID,
    CHECK_INTERVAL,
    MESSAGE_DELAY,
    INVITE_MESSAGE,
    WELCOME_MESSAGE,
    LOG_FILE,
    LOG_LEVEL,
    ENABLE_CONSOLE_LOG,
    DEBUG,
    DRY_RUN,
    USE_CSV_FILE,
    CSV_FILE_PATH,
    USER_IDS_LIST,
    TIMEOUT,
    MAX_RETRIES,
)

# ============================================
# SETUP LOGGING
# ============================================
logger = logging.getLogger("ClubhouseBot")
logger.setLevel(getattr(logging, LOG_LEVEL))

# File handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(getattr(logging, LOG_LEVEL))

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(getattr(logging, LOG_LEVEL))

# Formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
if ENABLE_CONSOLE_LOG:
    logger.addHandler(console_handler)

# ============================================
# CLUBHOUSE BOT CLASS
# ============================================
class ClubhouseBot:
    def __init__(self):
        self.api_key = CLUBHOUSE_API_KEY
        self.api_secret = CLUBHOUSE_API_SECRET
        self.user_id = CLUBHOUSE_USER_ID
        self.room_id = TARGET_ROOM_ID
        self.base_url = "https://www.clubhouseapi.com/api"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.sent_invites = set()
        self.session = requests.Session()
        
        logger.info("=" * 50)
        logger.info("🤖 Clubhouse Invite Bot Started")
        logger.info("=" * 50)
        logger.info(f"Room ID: {self.room_id}")
        logger.info(f"Check Interval: {CHECK_INTERVAL} seconds")
        logger.info(f"Debug Mode: {DEBUG}")
        logger.info(f"Dry Run Mode: {DRY_RUN}")

    def load_user_list(self):
        """Load user IDs from CSV file or config"""
        users = []
        
        if USE_CSV_FILE:
            try:
                with open(CSV_FILE_PATH, 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row:
                            users.append(row[0].strip())
                logger.info(f"✅ Loaded {len(users)} users from {CSV_FILE_PATH}")
            except FileNotFoundError:
                logger.warning(f"⚠️  CSV file not found: {CSV_FILE_PATH}")
                logger.info("Using USER_IDS_LIST from config instead")
                users = USER_IDS_LIST
        else:
            users = USER_IDS_LIST
        
        return users

    def make_request(self, endpoint, method="GET", data=None, retry=0):
        """Make API request with retry logic"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method == "GET":
                response = self.session.get(url, headers=self.headers, timeout=TIMEOUT)
            elif method == "POST":
                response = self.session.post(url, headers=self.headers, json=data, timeout=TIMEOUT)
            elif method == "PUT":
                response = self.session.put(url, headers=self.headers, json=data, timeout=TIMEOUT)
            
            if response.status_code in [200, 201]:
                return True, response.json()
            elif response.status_code == 429 and retry < MAX_RETRIES:
                logger.warning(f"⏳ Rate limited. Retrying... ({retry + 1}/{MAX_RETRIES})")
                time.sleep(TIMEOUT)
                return self.make_request(endpoint, method, data, retry + 1)
            else:
                logger.error(f"❌ API Error {response.status_code}: {response.text}")
                return False, None
                
        except requests.exceptions.Timeout:
            logger.error(f"❌ Request timeout for {endpoint}")
            return False, None
        except Exception as e:
            logger.error(f"❌ Request failed: {str(e)}")
            return False, None

    def send_invite(self, user_id):
        """Send invite message to a user"""
        if user_id in self.sent_invites:
            if DEBUG:
                logger.debug(f"⏭️  Already invited user: {user_id}")
            return False
        
        if DRY_RUN:
            logger.info(f"🧪 [DRY RUN] Would send invite to: {user_id}")
            logger.info(f"📝 Message: {INVITE_MESSAGE}")
            self.sent_invites.add(user_id)
            return True
        
        try:
            # API endpoint to send message/invite
            endpoint = f"/v1/users/{user_id}/invite"
            data = {
                "room_id": self.room_id,
                "message": INVITE_MESSAGE
            }
            
            success, response = self.make_request(endpoint, method="POST", data=data)
            
            if success:
                logger.info(f"✅ Invite sent to user: {user_id}")
                self.sent_invites.add(user_id)
                time.sleep(MESSAGE_DELAY)
                return True
            else:
                logger.error(f"❌ Failed to send invite to user: {user_id}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error sending invite to {user_id}: {str(e)}")
            return False

    def send_welcome_message(self, room_id=None):
        """Send welcome message to all room members"""
        if room_id is None:
            room_id = self.room_id
        
        if DRY_RUN:
            logger.info(f"🧪 [DRY RUN] Would send welcome message to room: {room_id}")
            logger.info(f"📝 Message: {WELCOME_MESSAGE}")
            return True
        
        try:
            # API endpoint to send room message
            endpoint = f"/v1/rooms/{room_id}/send_message"
            data = {
                "message": WELCOME_MESSAGE
            }
            
            success, response = self.make_request(endpoint, method="POST", data=data)
            
            if success:
                logger.info(f"✅ Welcome message sent to room: {room_id}")
                time.sleep(MESSAGE_DELAY)
                return True
            else:
                logger.error(f"❌ Failed to send welcome message to room: {room_id}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error sending welcome message: {str(e)}")
            return False

    def check_and_send_invites(self):
        """Check user list and send invites"""
        logger.info(f"🔍 Checking user list at {datetime.now().strftime('%H:%M:%S')}")
        
        users = self.load_user_list()
        
        if not users:
            logger.warning("⚠️  No users to invite!")
            return
        
        for user_id in users:
            self.send_invite(user_id)
            time.sleep(MESSAGE_DELAY)

    def run(self):
        """Main bot loop"""
        logger.info("🚀 Bot is running. Press Ctrl+C to stop.")
        
        try:
            # Send initial welcome message
            self.send_welcome_message()
            
            # Main loop
            while True:
                self.check_and_send_invites()
                
                if DEBUG:
                    logger.debug(f"⏰ Waiting {CHECK_INTERVAL} seconds until next check...")
                
                time.sleep(CHECK_INTERVAL)
                
        except KeyboardInterrupt:
            logger.info("\n⛔ Bot stopped by user")
        except Exception as e:
            logger.critical(f"❌ Critical error: {str(e)}")
            raise

    def stop(self):
        """Stop the bot gracefully"""
        logger.info("🛑 Stopping bot...")
        self.session.close()

# ============================================
# MAIN ENTRY POINT
# ============================================
if __name__ == "__main__":
    try:
        bot = ClubhouseBot()
        bot.run()
    except Exception as e:
        logger.critical(f"Failed to start bot: {str(e)}")
        exit(1)