import os


class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","18052289"))
    API_HASH = os.environ.get("API_HASH","552525f45a3066fee54ca7852235c19c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5192558668:AAHLhH7gCYZ8nKnmTL-zsvTL3qqINdqgbo0")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","Sematagbot")
    BOT_NAME = os.environ.get("BOT_NAME","𝗦Σ𝗠Δ 𝗧Δ𝗚𝗚Σ𝗥")
    BOT_ID = int(os.environ.get("BOT_ID","6118669969"))
    SUDO_USERS = os.environ.get("SUDO_USERS","1924693109").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT","SOQrup")
    OWNER_ID = int(os.environ.get("OWNER_ID","1924693109"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","Tenha055")
