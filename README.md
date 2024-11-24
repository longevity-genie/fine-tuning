# fine-tuning
Instruct lab fine-tuning

Quick setup for fine-tuning with InstructLab

## Environment

```bash
micromamba env create -f environment_cuda.yaml
```
After the environment is created, you can activate it with:
```bash
micromamba activate instructlab
which ilab #check the path to the ilab executable
ilab config init #initialize the configuration
```

when config starts provide th path to the folder where you made this fine-tunining repo on this machine. it is importan so it saves the taxonomy folders in the right directory

to fine-tune you need two models- the one you will fine tune and another one that will use the text to be trained with. in this exampale we used the tutorial from this [https://www.youtube.com/watch?v=4lguiHJHgfo]

you will have to download granite model from huggingface or something similar and put it in the models folder.

granite[https://huggingface.co/RichardErkhov/instructlab_-_granite-7b-lab-gguf/blob/main/granite-7b-lab.Q4_K_M.gguf]

also you will need to download merlinite model or something similar, reccomended in gguf format

merlinite[https://huggingface.co/instructlab/merlinite-7b-lab-GGUF/blob/main/merlinite-7b-lab-Q4_K_M.gguf]

the following command will show you whether the model you want to fine-tune is running properly and can be accessed as a server (according to the instructions from the tutorial). be aware that the name has to be quite specific.

```
ilab model serve --model-path /home/liviazaharia/sources/fine-tuning/models/granite-7b-lab.Q4_K_M.gguf #how to runthe interface

```
after that you must first create some sintetic data. istructlab is based in skills and knowledge- create the file you think you need (in this case we did the knowledge of open genes database) and then run the following command to see if there are any issues with the data.

```
ilab taxonomy diff #to see if there are issues withhow data is structured
```

second note- the way the model is run is, as i said, like a server, so as such it has an UI interface. that one is treated in a different repo but it can be installed and run following the instructions from here [https://docs.instructlab.ai/user-interface/playground_chat/]