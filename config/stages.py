import os


def get_stage():
    stages = {
        "dev": "https://dev-gs.qa-playground.com/api/v1",
        "release": "https://release-gs.qa-playground.com/api/v1"
    }

    STAGE = stages[os.environ["STAGE"]]
    return STAGE
