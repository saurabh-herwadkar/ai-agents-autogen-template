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

from ai_agents_autogen_template.agents.agents_defintions import user_proxy, manager
from ai_agents_autogen_template.groupchat.groupchat_definitons import groupchat, manager


# The main program to run
# Your crews related code will come here
def run():

    logging.info("--------Entering main method--------------")

    # Start the chat
    user_proxy.initiate_chat(
        manager,
        message="Find a latest paper about gpt-4 on arxiv and find its potential applications in software.",
    )

    logging.info("---------Leaving main method------------")
    return ""
