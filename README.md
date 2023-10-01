# Hindi To English Translation with Transformers

This repository contains Python code that utilizes the Hugging Face Transformers library to perform Hindi to English translation using a pre-trained model.

## Prerequisites

Before running the code, make sure to install the necessary Python packages by running the following commands:

```
pip install transformers
pip install huggingface_hub
huggingface-cli login
```
These commands will install the required packages and set up authentication for Hugging Face model access.

## Usage

Once you've completed the setup, you can use the provided Python script to perform Hindi to English translation. Here's an example of how to use it:

```
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M", use_auth_token=True, src_lang="eng_Latn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M", use_auth_token=True)

def return_translation(sentence):
    inputs = tokenizer(sentence, return_tensors="pt")
    translated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id["hin_Deva"], max_length=30)
    return tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]

# Example sentences for translation
sentence_one = "So even if it's a big video, I will clearly mention all the products."
sentence_two ="Definitely share your feedback in the comment section."
sentence_three = "I was waiting for my bag."

# Translate a sentence
result = return_translation(sentence_three)
print(result)
```

This code demonstrates how to load the pre-trained model, tokenize input sentences, and generate translations. You can replace sentence_three with your own sentences to perform translations.

Sample Output
For the provided example sentence:

```sentence_three = "I was waiting for my bag."```

The model output will be:

```मैं अपने बैग के लिए इंतजार कर रहा था.```

