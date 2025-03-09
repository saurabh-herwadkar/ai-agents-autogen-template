
import autogen
from ai_agents_autogen_template.agents.agents_defintions import user_proxy, coder, pm
from ai_agents_autogen_template.llm.llms_definitions import llm_config

groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)