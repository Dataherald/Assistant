from function import Function, Property
from dotenv import load_dotenv
from assistant import AIAssistant

load_dotenv()
class WeatherFunction(Function):
    def __init__(self):
        super().__init__(
            name="weather",
            description="Get the weather for a location",
            parameters=[
                Property(
                    name="location",
                    type="string",
                    required=True,
                    description="The location to get the weather for",
                )
            ],
        )
    def function(self, location: str):
        return f"The weather in {location} is sunny"


assistant = AIAssistant(
    instruction="You are a weather bot. Use the provided functions to answer questions.",
    model="gpt-3.5-turbo-1106",
    functions=[WeatherFunction()],
)
thread = assistant.create_thread()
message = assistant.chat(
    thread_id=thread.id, content="What is the weather in San Francisco?"
)
print(message)