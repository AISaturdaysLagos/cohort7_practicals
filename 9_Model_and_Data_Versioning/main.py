import json
import os
import tempfile

import mlflow
import yaml

STEPS = [
    "version_data",
    "cleaning",
    "data_validation",
    "data_split",
    "train_model"
]

ROOT_PATH = os.getcwd()
print(ROOT_PATH)


def main(config: dict):
    # TODO: Use `python-dotenv` to put these variables into the environment
    # then remove this bit of code
    os.environ["WANDB_PROJECT"] = config["main"]["project_name"]
    os.environ["WANDB_RUN_GROUP"] = config["main"]["experiment_name"]

    steps = config["main"]["steps"]
    active_steps = steps.split(",") if steps != "all" else STEPS
    print(active_steps)

    with tempfile.TemporaryDirectory() as tmp_dir:
        if "version_data" in active_steps:
            print("Running version_data step")
            _ = mlflow.run(
                os.path.join(ROOT_PATH, config["main"]["components_directory"], "version_data"),
                "main",
                parameters={
                    "data": config["etl"]["data"],
                    "artifact_name": "input_data.csv",
                    "artifact_type": "raw_data",
                    "artifact_description": "Insurance Prediction data"
                }
            )


if __name__ == "__main__":
    with open("config.yml", "r") as f:
        try:
            config = yaml.safe_load(f)
            print(config)
        except yaml.YAMLError as err:
            print(err)
            raise err

    main(config)
