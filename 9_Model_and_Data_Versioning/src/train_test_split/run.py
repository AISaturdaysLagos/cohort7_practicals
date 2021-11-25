"""
This script splits the provided data into train and validation datasets
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
    run = wandb.init(job_type="train_test_split")
    run.config.update(args)

    # --------------
    # YOUR CODE HERE
    # --------------


if __name__ == "_main__":
    parser = argparse.ArgumentParser(description="Split input into train and val sets")

    parser.add_argument(
        "--input_data",
        type= # TODO,
        default= # TODO,
        help= # TODO,
        required= # TODO,
    )

    parser.add_argument(
        "--val_size",
        type= # TODO,
        default= # TODO,
        help= # TODO,
        required= # TODO,
    )

    parser.add_argument(
        "--random_seed",
        type= # TODO,
        default= # TODO,
        help= # TODO,
        required= # TODO,
    )

    parser.add_argument(
        "--stratify_by",
        type= # TODO,
        default= # TODO,
        help= # TODO,
        required= # TODO,
    )


    args = parser.parse_args()
    go(args)
