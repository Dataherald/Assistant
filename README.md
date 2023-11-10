# OpenAI Assistant API Wrapper

This repository contains a lightweight, open-source codebase designed to work with OpenAI's Assistant API, enabling the creation of custom Assistants and functions. This project is currently under active development, and while fully functional, the Assistants may require further modifications to better suit your needs.

## Features

- **Custom Assistant Creation**: Easily create Assistants tailored to specific tasks or industries.
- **Enabling Custom Functions**: Create custom functions to be used by your Assistant.
- **Easy integration with OpenAI tools**: Integrate with OpenAI's tools, such as the code interpreter and retrieval, to further enhance your Assistant.
- **Lightweight**: The codebase only relies on a couple of packages, making it easy to install and use.

## Getting Started

To get started with this project, please follow the instructions below.

### Prerequisites

- An OpenAI API key. You can obtain one by signing up at [OpenAI](https://openai.com/).
- Python 3.6 or later.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Dataherald/Assistant
    ```

2. Navigate to the project directory:
    ```bash
    cd Assistant
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a .env file and set OPENAI_API_KEY = "your_api_key_here"

### Usage

This repository allows you to create custom functions that can be integrated with an AI Assistant. Below is an example of how to set up a custom function and use it with the Assistant.

#### Function Creation

To create a custom function, you must create a new class that inherits from the `Function` class.
Your class must have the following attributes:

1. `name`: The name of the function.
2. `description`: A description of the function.
3. `parameters`: A list of `Property` objects that define the parameters of the function. This is optional, and can be left blank if the function does not require any parameters.

Each Property object must have the following attributes:

1. `name`: The name of the parameter.
2. `description`: A description of the parameter.
3. `type`: The type of the parameter. This can be any type supported by OpenAI's API.
4. `required`: A boolean value indicating whether the parameter is required or not.

Finally, you have to implement the function method, which will be called when the function is invoked. The function method must accept the same number of parameters as the number of parameters defined in the `parameters` attribute.

Below is an example of a custom function that runs a SQL query on the Chinook database.

```python
from function import Function, Property

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
```

#### Assistant Creation

To create an Assistant, you must create an object of the `Assistant` class. The constructor of the class accepts the following parameters:
1. instruction (str): Instructions for the Assistant.
2. model (str): The model to be used by the Assistant.
3. use_retrieval (bool, optional): Whether to use retrieval tools. Defaults to False.
4. use_code_interpreter (bool, optional): Whether to use a code interpreter. Defaults to False.
5. file_ids (list[str], optional): List of file IDs passed to the ass. Defaults to None.
6. functions (list[Function], optional): List of Function instances the Assistant can use. Defaults to None.
7. assistant_name (str, optional): Name of the Assistant. Defaults to "AI Assistant".
8. assistant_description (str, optional): Description of the Assistant. Defaults to "An AI Assistant".
9. verbose (bool, optional): Enable verbose output. Defaults to False.

An example is provided below:

```python
from assistant import AIAssistant

assistant = AIAssistant(
    instruction="You are a SQL expert. User asks you questions about the Chinook database.",
    model="gpt-3.5-turbo-1106",
    functions=[RunSQLQuery()],
    use_code_interpreter=True,
    )
```

You can start chatting with the assistant by craeting a thread and calling the chat() function like below: 

```python
thread = assistant.create_thread()
user_input = ""
while user_input != "bye":
    print("\033[34mType your question or type bye to quit: ")
    user_input = input("\033[32mYou: ")
    message = assistant.chat(
    thread_id=thread.id, content=user_input
    )
    print(f"\033[33m{message}")
```

### Contribution

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

#### How to Contribute

1. **Fork the Project**: Click on the 'Fork' button at the top right corner of the repository page to create a copy of this project on your GitHub account.
2. **Create your Feature Branch**: In your forked repository, create a new branch for your feature using the command `git checkout -b feature/AmazingFeature`.
3. **Commit your Changes**: Make the desired changes in your branch and commit them using `git commit -m 'Add some AmazingFeature'`.
4. **Push to the Branch**: Upload your changes to GitHub using `git push origin feature/AmazingFeature`.
5. **Open a Pull Request**: Go to the 'Pull requests' tab in the original repository and click on 'New pull request'. Select your feature branch and submit the pull request with a description of your changes.


