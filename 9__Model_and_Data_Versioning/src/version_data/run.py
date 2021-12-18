"""
This script uploads the input data to W&B as an artifact

Author: Akintunde 'theyorubayesian' Oladipo
Date: 27 November 2021
"""
import argparse
import logging
import os
import time

import wandb

from wandb_utils.log_artifact import log_artifact

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=f"logs/{time.time()}.log",
    format="%(asctime)s - %(levelname)s - %(name)s - PID: %(process)d -  %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def go(args):
    run = wandb.init(job_type="Data Versioning")
    run.config.update(args)

    logger.info(os.getcwd())
    
    print(f"Uploading {args.artifact_name} to Weights & Biases")
    log_artifact(
        artifact_name=args.artifact_name,
        artifact_type=args.artifact_type,
        artifact_description=args.artifact_description,
        filename=os.path.join("data", args.data),
        wandb_run=run
    )
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Version input data")

    parser.add_argument(
        "--data",
        type=str,
        default="train_data.csv",
        help="Name of data sample to upload",
        required=True,
    )

    parser.add_argument(
        "--artifact_name",
        type=str,
        help="Name of output artifact",
        required=True,
    )

    parser.add_argument(
        "--artifact_type",
        type=str,
        help="Type of artifact uploaded",
        required=True,
    )

    parser.add_argument(
        "--artifact_description",
        type=str,
        help="A brief description of this artifact",
        required=True,
    )

    args = parser.parse_args()
    go(args)
