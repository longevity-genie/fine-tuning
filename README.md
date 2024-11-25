# InstructLab Fine-tuning Guide

A quick setup guide for fine-tuning models with InstructLab.

## Prerequisites

- micromamba or conda
- CUDA-capable GPU (recommended)
- At least 16GB RAM

## Environment Setup

1. Create and activate the environment (with micromamba or conda):
```bash
micromamba create -f environment_cuda.yaml
micromamba activate instructlab

# Verify installation
which ilab
```

2. Initialize InstructLab configuration:
```bash
ilab config init
```

### Configuration Tips

When running `ilab config init`:
- Set the taxonomy path to `./instructlab/taxonomy` within your project directory
- Choose the appropriate system profile based on your hardware (NVIDIA, AMD, etc.)
- Specify the path to your model file

## Required Models

You'll need two models for fine-tuning:

1. Base Model (to be fine-tuned):
   - [Granite 7B](https://huggingface.co/RichardErkhov/instructlab_-_granite-7b-lab-gguf/blob/main/granite-7b-lab.Q4_K_M.gguf)
   - Place in `./models/` directory

2. Training Assistant Model:
   - [Merlinite 7B](https://huggingface.co/instructlab/merlinite-7b-lab-GGUF/blob/main/merlinite-7b-lab-Q4_K_M.gguf)
   - Place in `./models/` directory

## Usage

1. Test model serving:
```bash
ilab model serve --model-path ./models/granite-7b-lab.Q4_K_M.gguf
```

2. Validate taxonomy data:
```bash
ilab taxonomy diff
```

## Web Interface

For a graphical interface, follow the [Playground Chat setup instructions](https://docs.instructlab.ai/user-interface/playground_chat/)

To set it up locally:

1. Install pnpm, npm or deno

2. Clone and run the UI:
```bash
git clone https://github.com/instructlab/ui
cd ui
npm install
npm run dev
```

## Additional Resources

- [Video Tutorial](https://www.youtube.com/watch?v=4lguiHJHgfo)
- [InstructLab Documentation](https://docs.instructlab.ai)