Sure! Here is a simple README for your program:

---

# OpenAI Chatbot

This is a basic implementation of a chatbot using OpenAI's GPT-3.5-turbo model. This chatbot takes user input, sends it to the OpenAI API, and prints out the AI's response.

## Prerequisites

To use this chatbot, you'll need:

- Python 3.6 or higher
- An OpenAI API key. Sign up on [OpenAI's website](https://www.openai.com) to get one.

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/yourusername/yourrepository.git
    ```

2. Install the OpenAI Python client:
    ```sh
    pip install openai
    ```

3. Set your OpenAI API key as an environment variable:
    ```sh
    export OPENAI_API_KEY='your-api-key'
    ```

## Usage

To start the chatbot, run:
```sh
python main.py
```

You can also use the `-tokens` flag to display the token usage after each AI response:
```sh
python main.py -tokens
```

## Note

This is a basic implementation of a chatbot. It does not handle multi-turn conversations, manage tokens to ensure responses do not exceed maximum token limits, or handle API errors gracefully.

---

Please replace `'your-api-key'` with your actual OpenAI API key, and `https://github.com/yourusername/yourrepository.git` with the actual URL of your GitHub repository. The `-tokens` flag is optional, and can be used to display the token usage of the model's responses.