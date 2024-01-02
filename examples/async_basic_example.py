import asyncio
import sys

from re_gpt import AsyncChatGPT

# consts
session_token = "__Secure-next-auth.session-token here"
conversation_id = None  # Set it to the conversation ID if you want to continue an existing chat or None to create a new chat

# If the Python version is 3.8 or higher and the platform is Windows, set the event loop policy
if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    # Create an asynchronous ChatGPT instance using the session token from the config file
    async with AsyncChatGPT(session_token=session_token) as chatgpt:
        # Get user input for the chat prompt
        prompt = input("Enter your prompt: ")

        # Continue the existing chat using conversation_id or create a new chat if conversation_id is none
        if conversation_id:
            conversation = chatgpt.get_conversation(conversation_id)
        else:
            conversation = chatgpt.create_new_conversation()

        # Iterate through the messages received from the chatgpt and print it
        async for message_chunk in conversation.chat(prompt):
            print(message_chunk["content"], flush=True, end="")


if __name__ == "__main__":
    # Run the asynchronous main function using asyncio.run()
    asyncio.run(main())
