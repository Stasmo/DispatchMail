from dotenv import load_dotenv
import os
import importlib.util
import sys

# Load the local credentials.py file explicitly
credentials_path = os.path.join(os.path.dirname(__file__), 'credentials.py')
spec = importlib.util.spec_from_file_location('local_credentials', credentials_path)
credentials = importlib.util.module_from_spec(spec)
spec.loader.exec_module(credentials)

load_dotenv()

# SQLite configuration - use absolute path so both daemon and API use the same database
#note project root is one level up from web-app so we need to go up one level
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
DATABASE_PATH = os.getenv('DATABASE_PATH', os.path.join(PROJECT_ROOT, 'dmail.db'))

# Number of days to look back when fetching emails on startup
# if no previous timestamp is stored.
LOOKBACK_DAYS = int(os.getenv('LOOKBACK_DAYS', '1'))

# OpenAI API Config
OPENAI_API_KEY = credentials.OPENAI_API_KEY
OPENAI_API_BASE = credentials.OPENAI_API_BASE