#! /bin/bash
# it is assumed that you run script from the root directory of the project
eval "$(micromamba shell hook --shell bash)"
micromamba activate instructlab

source .env

ilab serve --model-path "models/granite-7b-lab.Q4_K_M.gguf"