"""
This step performs feature engineering before modelling is done
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
    run = wandb.init(job_type="feature_engineering")
    run.config.update(args)

    # --------------
    # YOUR CODE HERE
    # --------------


if __name__ == "_main__":
    parser = argparse.ArgumentParser(description="Engineers features in data")

    parser.add_argument(
        "--min_samples_leaf",
        type= # TODO,
        default= # TODO,
        help= # TODO,
        required= # TODO,
    )

    parser.add_argument(
        "--smoothing",
        type= # TODO,
        default= # TODO,
        help= # TODO,
        required= # TODO,
    )


    args = parser.parse_args()
    go(args)
