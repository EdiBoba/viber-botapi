__version__ = "1.0.0"

import asyncio
import sys

from . import types
from . import utils

if sys.platform.startswith('win'):
    if sys.version_info[0] == 3 and sys.version_info[1] >= 8:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())