from dotenv import load_dotenv
from assistant import AIAssistant

load_dotenv()

if __name__ == "__main__":
    assistant = AIAssistant(
    instruction=""" You are a helpful agent that helps user with their question about LLMs.""",
    model="gpt-4-1106-preview",
    use_retrieval=True,
    verbose=True,
    )
    file_id = assistant.upload_file("assistants_files/llama2_paper.pdf")
    assistant.chat(file_ids=[file_id])