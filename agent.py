from swarm import Swarm, Agent

# Initialize Swarm client
client = Swarm()

conversation_history = []

def transfer_to_agent_exit():
    return agent_exit

main_agent = Agent(
    name="Loly-MIDI",
    instructions="Respond in Spanish, don't use asterisk (*) on your responses to change format, your text is lisened not readed.",
    model="loly:latest",
)
agent_exit = Agent(
    name="Loly-exit",
    instructions="Identify if any sentence aims to end the conversation. If you identify that the conversation is intended to be ended, respond with the word 'exit'",
    model="loly:latest"
)




def agent_response(user_input):
    conversation_history.append({'role': 'user', 'content': user_input})
    
    response = client.run(
        agent=main_agent,
        messages=conversation_history
    )
    response_content = response.messages[-1]["content"]
    conversation_history.append({'role': 'assistant', 'content': response_content})
    
    print(f"\n\n\n {response_content} \n\n\n")
    
    exit_control_response = client.run(
        agent=agent_exit,
        messages=[{"role": "user", "content": user_input }]
    )
    exit_control_response_content = exit_control_response.messages[-1]["content"]

    if exit_control_response_content == "exit":
        return "exit"
    return  response_content
