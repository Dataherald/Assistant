from function import Function, Property
from dotenv import load_dotenv
from assistant import AIAssistant
import sqlite3

load_dotenv()


class GetDBSchema(Function):
    def __init__(self):
        super().__init__(
            name="get_db_schema",
            description="Get the schema of the Chinook database",
        )

    def function(self):
        conn = sqlite3.connect('Chinook.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
        create_statements = cursor.fetchall()
        conn.close()
        return '\n\n'.join([statement[0] for statement in create_statements])
    
class RunSQLQuery(Function):
    def __init__(self):
        super().__init__(
            name="run_sql_query",
            description="Run a SQL query on the Chinook database",
            parameters=[
                Property(
                    name="query",
                    description="The SQL query to run",
                    type="string",
                    required=True,
                ),
            ]
        )

    def function(self, query):
        conn = sqlite3.connect('Chinook.sqlite')
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return '\n'.join([str(result) for result in results])
    
if __name__ == "__main__":
    assistant = AIAssistant(
    instruction="You are a SQL expert. User asks you questions about the Chinook database.",
    model="gpt-3.5-turbo-1106",
    functions=[GetDBSchema(), RunSQLQuery()],
    verbose=True
    )
    thread = assistant.create_thread()
    user_input = ""
    while user_input != "bye":
        print("\033[34mType your question or type bye to quit: ")
        user_input = input("\033[32mYou: ")
        message = assistant.chat(
        thread_id=thread.id, content=user_input
        )
        print(f"\033[33m{message}")