from just_agents import llm_options
from just_agents.base_agent import BaseAgent
from dotenv import load_dotenv
from typing import Any
import json
import os
import litellm

#hosted_vllm

GRANITE_7B_LAB: dict = {
    #supports both text and vision
    "model": "models/granite-7b-lab.Q4_K_M.gguf",
    "api_base": "http://127.0.0.1:8000",
    "temperature": 0.0,
    "tools": []
}
"""
This example shows how a function can be used to call a function which potentially can have an external API call.
"""
def get_current_weather(location: str):
    """Gets the current weather in a given location"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": "celsius"})
    elif "san francisco" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "72", "unit": "fahrenheit"})
    elif "paris" in location.lower():
        print("IT WORKS!==================")
        return json.dumps({"location": "Paris", "temperature": "22", "unit": "celsius"})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})

#models/granite-7b-lab.Q4_K_M.gguf

if __name__ == "__main__":
    load_dotenv(override=True)
    
    llm_options = {
        "model": "litellm_proxy/granite",
        "temperature": 0.0,
        "api_base": "http://localhost:4000"
    }
    system_prompt = """
    You are a helpful assistant that can answer questions about the weather.
    You can use the following tools to answer questions:
    get_current_weather(location: str) -> dict
    this function always return current weather.
    
    Please, use the tool all the time to answer questions about the weather, do not ask the user for additional information.
    """
    agent = BaseAgent(llm_options=llm_options, tools=[get_current_weather], system_prompt=system_prompt)
    test = agent.query("What is the weather in Paris now?")
    print(test)
