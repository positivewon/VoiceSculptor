from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import soundfile as sf
from xcodec2.modeling_xcodec2 import XCodec2Model
import os
import json
from tqdm import tqdm

def ids_to_speech_tokens(speech_ids):
 
    speech_tokens_str = []
    for speech_id in speech_ids:
        speech_tokens_str.append(f"<|s_{speech_id}|>")
    return speech_tokens_str

def extract_speech_ids(speech_tokens_str):
 
    speech_ids = []
    for token_str in speech_tokens_str:
        if token_str.startswith('<|s_') and token_str.endswith('|>'):
            num_str = token_str[4:-2]

            num = int(num_str)
            speech_ids.append(num)
        else:
            print(f"Unexpected token: {token_str}")
    return speech_ids


model_path = ""
device = "cuda"
xcodec2_model_path = ""
out_path = "./output"
version = "llasa_3b_instruct_zh"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
model.eval() 
model.to(device)
Codec_model = XCodec2Model.from_pretrained(xcodec2_model_path)
Codec_model.eval().to(device)  
output_dir = os.path.join(out_path, version)
os.makedirs(output_dir,exist_ok=True)

text = "这是一位幼儿园女教师，用甜美明亮的嗓音，以极慢且富有耐心的语速，带着温柔鼓励的情感，用标准普通话给小朋友讲睡前故事，音量轻柔适中，咬字格外清晰。<|endofprompt|>月亮婆婆升上天空啦，星星宝宝都困啦。小白兔躺在床上，盖好小被子，闭上眼睛。兔妈妈轻轻地唱着摇篮曲：睡吧睡吧，我亲爱的宝贝。"
out_name = "examples_nvjiaoshi"
#TTS start!
with torch.no_grad():

    formatted_text = f"<|TEXT_UNDERSTANDING_START|>{text}<|TEXT_UNDERSTANDING_END|>"

    # Tokenize the text
    chat = [
        {"role": "user", "content": "Convert the text to speech:" + formatted_text},
        {"role": "assistant", "content": "<|SPEECH_GENERATION_START|>"}
    ]

    input_ids = tokenizer.apply_chat_template(
        chat, 
        tokenize=True, 
        return_tensors='pt', 
        continue_final_message=True
    )
    input_ids = input_ids.to(device)
    speech_end_id = tokenizer.convert_tokens_to_ids('<|SPEECH_GENERATION_END|>')

    # Generate the speech autoregressively
    outputs = model.generate(
        input_ids,
        max_length=2048,  # We trained our model with a max length of 2048
        eos_token_id= speech_end_id ,
        do_sample=True, 
        top_p=0.95,          
        temperature=0.9,    
    )
    # Extract the speech tokens
    generated_ids = outputs[0][input_ids.shape[1]:-1]

    speech_tokens = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)   

    # Convert  token <|s_23456|> to int 23456 
    speech_tokens = extract_speech_ids(speech_tokens)

    speech_tokens = torch.tensor(speech_tokens).to(device).unsqueeze(0).unsqueeze(0)

    # Decode the speech tokens to speech waveform
    gen_wav = Codec_model.decode_code(speech_tokens) 

sf.write(f"{output_dir}/{out_name}.wav", gen_wav[0, 0, :].cpu().numpy(), 16000)
