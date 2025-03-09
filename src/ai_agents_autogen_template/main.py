# Imports
from dotenv import load_dotenv
import os

# Load environment
load_dotenv()

import logging

# Load Agent ops
import agentops

agentops.init()

# Set logging level
logging.getLogger().setLevel(logging.INFO)

import autogen
from autogen import AssistantAgent, UserProxyAgent

llm_config = {"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}

assistant = AssistantAgent("assistant", llm_config=llm_config)

user_proxy = UserProxyAgent(
    "user_proxy",
    code_execution_config={
        "executor": autogen.coding.LocalCommandLineCodeExecutor(work_dir="coding")
    },
)


# The main program to run
# Your crews related code will come here
def run():

    logging.info("--------Entering main method--------------")

    # Start the chat
    user_proxy.initiate_chat(
        assistant,
        message="Plot a chart of NVDA and TESLA stock price change YTD.",
    )

    logging.info("---------Leaving main method------------")
    return ""
