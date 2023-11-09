from openai import Client
import time
from function import Function, FunctionCall, Property
from dotenv import load_dotenv

load_dotenv()
client = Client()
class WeatherFunction(Function):
    def __init__(self):
        super().__init__(
            name="weather",
            description="Get the weather for a location",
            parameters=[
                Property(name="location", type="string", required=True, description="The location to get the weather for")
            ]
        )
    
    def function(self, location: str):
        return f"The weather in {location} is sunny"

weather_function = WeatherFunction()

print(weather_function.to_dict())

assistant = client.beta.assistants.create(
  instructions="You are a weather bot. Use the provided functions to answer questions.",
  model="gpt-3.5-turbo-1106",
  tools=[{"type": "function", "function": weather_function.to_dict()}]
)

thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What is the weather in San Francisco?"
)
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
)
run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)
while run.status == "in_progress":
    run = client.beta.threads.runs.retrieve(
      thread_id=thread.id,
      run_id=run.id
    )
    time.sleep(1)
print(run)
print("================")
messages = client.beta.threads.messages.list(
  thread_id=thread.id
)
print(messages)
