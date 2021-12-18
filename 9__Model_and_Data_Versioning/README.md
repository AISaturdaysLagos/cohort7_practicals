

# Setup and Installation
* If you are using Windows, it is recommended that you either:
    - Work through Git Bash in your VS Code Terminal.
    - Install the Ubuntu 20.04 LTS as Linux Distribution. You can find instructions here: [Install WSL](https://docs.microsoft.com/en-us/windows/wsl/install). 
* Install Anaconda or Miniconda on your laptop. Then create an environment for this project.
```sh
conda env create --file conda.yml
conda activate insurtech
```
To understand how the `conda env create`command works, run `conda env create --help`.
* Create a [Weights & Biases](https://wandb.ai/) account
* Get the API key for your Weights & Biases account [here](https://wandb.ai/authorize) then login
```sh
wandb login <your_API_Key>
```

## Cookie Cutter
Cookiecutter allows us to create template steps that can then be edited. It standardizes projects and allows faster development by allowing engineers focus on what is important. We have created a template step in [pipeline-step-cookie](pipeline-step-cookie). To create a new step:
```sh
$ cookiecutter pipeline-step-cookie -o src
```
## Cleaning out mlflow environments
If there's an issue with any of the environments mlflow creates, you can get a list by executing:
```
conda env list | grep mlflow | cut -f 1 -d " "
```
You can remove all environments with names that start with `mlflow` as follows:
```
for e in $(conda env list | grep mlflow | cut -f 1 -d " "); do conda uninstall --name $e --all -y; done
```
Be careful with this command! 

# Resources
1. [How we build MLflow projects and rapidly iterate over them](https://medium.com/hellogetsafe/how-we-build-mlflow-projects-and-rapidly-iterate-over-them-90009de824cf)
2. [Project templates and Cookiecutter](https://medium.com/worldsensing-techblog/project-templates-and-cookiecutter-6d8f99a06374)
3. [Target Encoding Vs. One-hot Encoding with Simple Examples](https://medium.com/analytics-vidhya/target-encoding-vs-one-hot-encoding-with-simple-examples-276a7e7b3e64)