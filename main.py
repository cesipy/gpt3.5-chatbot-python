import argparse
import openai
import os

def parse_arguments():
    # create the top-level parser to handle -token flag
    parser = argparse.ArgumentParser()
    parser.add_argument("-tokens", action="store_true", help="show token usage")
    return parser.parse_args()

def get_response(chat_history):
    # receive generated response
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=chat_history)
    chat_history.append({
        'role':'assistant',
        'content': response.choices[0].message.content
    })
    return response

def main():
    args = parse_arguments()

    # get openai key
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # initialize empty array for history
    chat_history = []

    # initial message
    # is appended to chat_history
    # 'user' ... user messages
    # 'assistant' ... assistant messages
    #
    # 'content'   ... here you can add any other starting text
    # like 'act like a ...'
    message = {
        'role': 'user',
        'content': 'hello '
    }
    chat_history.append(message)

    response = get_response(chat_history)
    
    # repeat until too many tokens or program is exited
    while True:
        try:
            # receive input and append to chat_history
            user_input = input(">>> ")

            message = {
                'role': 'user',
                'content': user_input
            }

            chat_history.append(message)
            response = get_response(chat_history)

            if args.tokens:
                print(response.choices[0].message.content, end=' ')
                print(f"({response.usage.total_tokens} tokens)")
                print()
            else:
                print(response.choices[0].message.content)
                print()
        except Exception as e:
            print("Error occurred: ", e)
            break

if __name__ == "__main__":
    main()
