#! /bin/bash
# it is assumed that you run script from the root directory of the project
# Ensure we're in the right micromamba environment
eval "$(micromamba shell hook --shell bash)"
micromamba activate instructlab

source .env

litellm --config config/litellm_config.yaml