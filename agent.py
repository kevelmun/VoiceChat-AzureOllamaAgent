from datetime import datetime
from swarm import Swarm, Agent
from duckduckgo_search import DDGS

current_date = datetime.now().strftime("%Y-%m")

# Initialize Swarm client
client = Swarm()


agent = Agent(
    name="Loly-MIDI",
    instructions="Respond in Spanish, don't use asterisk (*) on your responses to change formt, your text is lisened not readed. You are an Agent called Loly-MIDI, serving as an educational tool with the objective to improve the development of social and cognitive skills in children, focusing on ASD.",
    model="llama3.2"
    )


def agent_response(user_input):
    response = client.run(
        agent=agent,
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    return  response.messages[-1]["content"]
