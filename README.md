




## About The Project

This project can be used to integrate OpenAI's ChatGPT services into your python code. You can use this project to prompt ChatGPT for responses directly from python, without using an official API key.

This can be useful if you want to use ChatGPT API without a [ChatGPT Plus](https://openai.com/blog/chatgpt-plus) account.

### Inspiration

ChatGPT has an official API which can be used to interface your Python code to it, but it needs to be used with an API key. This API key can only be obtained if you have a [ChatGPT Plus](https://openai.com/blog/chatgpt-plus) account, which requires $20/month (as of 05/11/2023). But you can use ChatGPT for free, using the [ChatGPT web interface](https://chat.openai.com/). This project aims to interface your code to ChatGPT web version so you can use ChatGPT in your Python code without using an API key.

### How it works

[ChatGPT](https://chat.openai.com/) web interface's requests have been reverse engineered, and directly integrated into Python requests. Hence, any requests made using this script is a simulated as a request made by a user directly on the website. Hence, it is free and needs no API key.

### Built Using

* [![Python][python-badge]][python-url]

## Getting Started

### Prerequisites

* Python >= 3.9

### Installation

```sh
pip install re-gpt
```
## Usage

### Basic example

```python
from re_gpt import SyncChatGPT

session_token = "__Secure-next-auth.session-token here"
conversation_id = None # conversation ID here


with SyncChatGPT(session_token=session_token) as chatgpt:
    prompt = input("Enter your prompt: ")

    if conversation_id:
        conversation = chatgpt.get_conversation(conversation_id)
    else:
        conversation = chatgpt.create_new_conversation()

    for message in conversation.chat(prompt):
        print(message["content"], flush=True, end="")

```

### Basic async example
```python
import asyncio
import sys

from re_gpt import AsyncChatGPT

session_token = "__Secure-next-auth.session-token here"
conversation_id = conversation_id = None # conversation ID here

if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    async with AsyncChatGPT(session_token=session_token) as chatgpt:
        prompt = input("Enter your prompt: ")

        if conversation_id:
            conversation = chatgpt.get_conversation(conversation_id)
        else:
            conversation = chatgpt.create_new_conversation()

        async for message in conversation.chat(prompt):
            print(message["content"], flush=True, end="")


if __name__ == "__main__":
    asyncio.run(main())
```

## More Examples

For a more complex example, check out the [examples](/examples) folder in the repository.

### Obtaining The Session Token

1. Go to <https://chat.openai.com/chat> and log in or sign up.
2. Open the developer tools in your browser.
3. Go to the `Application` tab and open the `Cookies` section.
4. Copy the value for `__Secure-next-auth.session-token` and save it.

## TODO

* [x] Add more examples
* [ ] Add better error handling
* [ ] Implement a function to retrieve all ChatGPT chats
* [ ] Improve documentation

## Contributing

Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

