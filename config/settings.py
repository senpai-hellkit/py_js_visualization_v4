import os
from dotenv import load_dotenv
from typing import Dict


load_dotenv()
env: Dict[str, str] = eval(os.getenv('PRODUCTION_DB'))
