This is the code and data repository for '[LLM Name]: Designing Personalized and Workforce-Aligned Cybersecurity Curricula Using Fine-Tuned LLMs'.
Our methodology is designed to automate cybersecurity curriculum analysis, leveraging the power of fine-tuned LLMs. 
It consists of two parts: PreprocessLM, based on the Qwen-2.5-7B model, and ClassifyLM, based on a fine-tuned BERT. 
For more details on our fine-tuning strategy, see [this file](https://github.com/arthurnijdam/LLMedu/tree/main/finetuning.pdf). A file with supplementary methodological information and results can be found [here](https://github.com/arthurnijdam/LLMedu/tree/main/supplementary.pdf).

# Get started 
1. Clone or download this repository
2. Create a conda environment with all necessary dependencies by running `conda create --name <env> --file package_list.txt'
3. (optional) re-run the [preprocessing](https://github.com/arthurnijdam/LLMedu/tree/main/data/Preprocessing.ipynb) and the generation of a [synthetic dataset based on CSEC2017](https://github.com/arthurnijdam/LLMedu/tree/main/data/create_csec2017_dataset.ipynb)
4. Fine-tune the [BERT model ](https://github.com/arthurnijdam/LLMedu/tree/main/baselines/Transformers.ipynb) or any other [baseline](https://github.com/arthurnijdam/LLMedu/tree/main/baselines/)

# Data 
Multiple data sources were used for this project, and all data is included in this repository under [data/](https://github.com/arthurnijdam/LLMedu/tree/main/data/).
The most notable resources are: 
1. The NICE framework, [v1.0.0. (2017)](https://github.com/arthurnijdam/LLMedu/blob/main/data/NICE%20Framework%20Components%20v1.0.0(1).xlsx), [v2.0.0. (2025)](https://github.com/arthurnijdam/LLMedu/blob/main/data/NICE%20Framework%20Components%20v2.0.0(2).xlsx), and the [annotations provided for the v1.0.0. KDs by Ramezanian et al](https://github.com/arthurnijdam/LLMedu/blob/main/data/Mappings_between_CSEC2017_and_the_NICE_Framework.xlsx).
2. [9 real-world courses + their annotations by Expert Group X + Control Group A](https://github.com/arthurnijdam/LLMedu/blob/main/data/Topics_Annotation.xlsx).
3. [Knowledge Descriptions from the v2.0.0. NICE framework, annotated by Expert Group X + Control Group B](https://github.com/arthurnijdam/LLMedu/blob/main/data/new_random_50_kd_mappings_with_AI_mappings2.xlsx). 

# Evaluation 
After completing the steps listed in 'Get Started', [LLM NAME] can be applied to several scenarios, also listed in our paper. 
First, [role-based weights](https://github.com/arthurnijdam/LLMedu/blob/main/eval/compute_role-based_weights.ipynb) for each NICE job role can be computed. 
Then, the same process can be applied to real-world [courses](https://github.com/arthurnijdam/LLMedu/blob/main/eval/Course_analysis.ipynb), such that a given curriculum can be matched to the NICE framework. 

# License 
[LLM NAME] is distributed under the terms of the [Creative Commons-BY-NC-ND license](https://github.com/santisoler/cc-licenses/blob/main/LICENSE-CC-BY-NC-ND). 


