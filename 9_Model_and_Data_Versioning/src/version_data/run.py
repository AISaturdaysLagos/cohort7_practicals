"""
This script uploads the input data to W&B as an artifact
"""
import argparse
import logging
import time

import wandb

logging.basicConfig(
    filename=f"logs/ofurufu_{time.time()}.log",
    format="%(asctime)s - %(levelname)s - %(name)s - PID: %(process)d -  %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def go(args):
    run = wandb.init(job_type="Data Versioning")
    run.config.update(args)

    # --------------
    # YOUR CODE HERE
    # --------------


if __name__ == "_main__":
    parser = argparse.ArgumentParser(description="Version input data")

    parser.add_argument(
        "--data",
        type= # TODO,
        default= # TODO,
        help= # TODO,
        required= # TODO,
    )

    parser.add_argument(
        "--artifact_name",
        type= # TODO,
        default= # TODO,
        help= # TODO,
        required= # TODO,
    )

    parser.add_argument(
        "--artifact_type",
        type= # TODO,
        default= # TODO,
        help= # TODO,
        required= # TODO,
    )

    parser.add_argument(
        "--artifact_description",
        type= # TODO,
        default= # TODO,
        help= # TODO,
        required= # TODO,
    )


    args = parser.parse_args()
    go(args)
