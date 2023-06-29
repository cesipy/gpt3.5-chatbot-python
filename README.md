

# OpenAI Chatbot

This is a basic implementation of a chatbot using OpenAI's GPT-3.5-turbo model. This chatbot takes user input, sends it to the OpenAI API, and prints out the AI's response.

## Prerequisites

To use this chatbot, you'll need:

- Python 3.6 or higher
- An OpenAI API key. Sign up on [OpenAI's website](https://www.openai.com) to get one.

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/cesipy/gptchat-with-history.git
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

## Still to Do:

    - limit the message_history, so max tokens aren't reached
    - handle exceptions
    - exit gracefully

