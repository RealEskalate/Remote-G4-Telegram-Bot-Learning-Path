import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# # load yaml config
# with open(config_dir / "config.yml", 'r') as f:
#     config_yaml = yaml.safe_load(f)

# # load .env config
# config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
telegram_token = "Token"
openai_api_key = "api_key"
openai_api_base = None
allowed_telegram_usernames = []
new_dialog_timeout = 600
enable_message_streaming = True
return_n_generated_images = 1
image_size = "512x512" 
n_chat_modes_per_page = 5
mongodb_uri = ""

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# # files
# help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
