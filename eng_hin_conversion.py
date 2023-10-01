
#pip install transformers
#pip install huggingface_hub
#huggingface-cli login 

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M", use_auth_token=True, src_lang="eng_Latn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M", use_auth_token=True)

def return_translation(sentence):
    inputs = tokenizer(sentence, return_tensors="pt")
    translated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id["hin_Deva"], max_length=30)
    return tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]


sentence_one = "So even if it's a big video, I will clearly mention all the products."
#model output = तो भले ही यह एक बड़ा वीडियो हो, मैं स्पष्ट रूप से सभी उत्पादों का उल्लेख करूंगा।

sentence_two ="Definitely share your feedback in the comment section."
#mode_output =  टिप्पणी अनुभाग में अपनी प्रतिक्रियाओं को साझा करें।

sentence_three = "I was waiting for my bag."
#model_output = मैं अपने बैग के लिए इंतजार कर रहा था.

result = return_translation(sentence_three)
print(result)
