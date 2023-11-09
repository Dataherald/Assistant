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


