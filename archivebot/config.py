"""Config values for archivebot."""
import os
import sys
import toml

default_config = {
    "telegram": {
        "userbot": True,
        "api_key": "your_telegram_api_key (empty if in userbot mode)",
        "phone_number": "your_phone_number (empty if not in userbot mode)",
        "app_api_id": 0,
        "app_api_hash": "apihash",
    },
    "database": {"sql_uri": "sqlite:///archivebot.db",},
    "logging": {"sentry_enabled": False, "sentry_token": "",},
    "download": {
        "allowed_types": ["document", "photo"],
        "target_dir": "/home/user/archivebot/",
    },
}

config_path = os.path.expanduser("~/.config/archivebot.toml")

if not os.path.exists(config_path):
    with open(config_path, "w") as file_descriptor:
        toml.dump(default_config, file_descriptor)
    print("Please adjust the configuration file at '~/.config/archivebot.toml'")
    sys.exit(1)
else:
    config = toml.load(config_path)
