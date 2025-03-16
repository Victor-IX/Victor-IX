import datetime
import os

# GitHub Credentials
USER_NAME = "Victor-IX"
HEADERS = {"authorization": "token " + os.environ["ACCESS_TOKEN"]}

# Age
# Year, month, day
BIRTHDATE = datetime.datetime(2000, 6, 29)

# Default cube counter
# Date when starting using blender, year, month, day
DATE = datetime.datetime(2014, 12, 15)
# Estimated number of default cubes removed per day
CUBES_PER_DAY: int = 1

# Download count
# Repository URL
REPO: str = "https://api.github.com/repos/victor-ix/blender-launcher-v2"
