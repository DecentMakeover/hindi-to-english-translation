# Hindi To English Translation

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

```python eng_hin_conversion.py```

The code loads the pre-trained model, tokenizes input sentences, and generates translations. You can replace sentence_three with your own sentences to perform translations.

## Sample Output

For the provided example sentence:

```sentence_three = "I was waiting for my bag."```

The model output will be:

```मैं अपने बैग के लिए इंतजार कर रहा था.```

