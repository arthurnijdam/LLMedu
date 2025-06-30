import json
from tqdm import tqdm

def submit_message_LLM(model, messages, tokenizer, device): 
    text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)
    
    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    
    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]


def topic_prompt(topic, description):
        """
        Formats a topic and description into a list of message dictionaries for the pipeline.
        """
        #options_str = ', '.join([f"{key}) {value}" for key, value in answers.items()])
        instructions = (
            "You are a helpful AI assistant.\n"
            "Instructions:\n"
            "a. Carefully read the topic and description .\n"
            "b. Give a list of all subtopics in the description .\n"
            "c. Do NOT include any explanation or additional text in the response.\n"
            #"d. Always return the answer in this XML format: '<xml>answer</xml>'. "
            #"For example, if the correct answer is D, then return <xml>D</xml>.\n\n"
        )
    
        messages = [
            {"role": "system", "content": instructions},
            {"role": "user", "content": f"#topic : {topic}\n #description: {description}"}
        ]
        return messages