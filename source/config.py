import datetime
import os

# GitHub Credentials
# Fine-grained personal access token with All Repositories access:
# Account permissions: read:Followers, read:Starring, read:Watching
# Repository permissions: read:Commit statuses, read:Contents, read:Issues, read:Metadata, read:Pull Requests
# Issues and pull requests permissions not needed at the moment, but may be used in the future
USER_NAME = "Victor-IX"
PAT = os.environ["ACCESS_TOKEN"]
HEADERS = {"authorization": "token " + PAT}

GRAPHQL_ENDPOINT = "https://api.github.com/graphql"

# Age
# Year, month, day
BIRTHDATE = datetime.datetime(2000, 6, 29)

# Default cube counter
# Date when starting using blender, year, month, day
DATE = datetime.datetime(2014, 12, 15)
# Estimated number of default cubes removed per day
CUBES_PER_DAY: int = 1

# Maya crash counter
# Date when starting using maya, year, month, day
MAYA_CRASH_DATE = datetime.datetime(2025, 5, 5)
# Estimated number of maya crashes per weekday (Monday to Friday)
MAYA_CRASHES_PER_DAY: int = 1

# Work hours counters
# Nvizzio
NVIZZIO_START = datetime.datetime(2021, 9, 13)
NVIZZIO_END = datetime.datetime(2022, 4, 22)
NVIZZIO_HOURS_PER_WEEK: float = 40
NVIZZIO_VACATION_DAYS_PER_YEAR: float = 10

# Metric Empire
METRIC_EMPIRE_START = datetime.datetime(2022, 4, 25)
METRIC_EMPIRE_END = datetime.datetime(2025, 5, 3)
METRIC_EMPIRE_HOURS_PER_WEEK: float = 40
METRIC_EMPIRE_VACATION_DAYS_PER_YEAR: float = 25

# Star Citizen (leave END as None to count up to today)
STAR_CITIZEN_START = datetime.datetime(2025, 5, 5)
STAR_CITIZEN_END = None
STAR_CITIZEN_HOURS_PER_WEEK: float = 40
STAR_CITIZEN_VACATION_DAYS_PER_YEAR: float = 30

# Download count
# Repository URL
REPO_NAME: str = "blender-launcher-v2"

REPO_IGNORE_LIST = ["winget-pkgs", "Blender-Launcher-V2-Backup"]
