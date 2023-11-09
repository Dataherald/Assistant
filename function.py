from abc import abstractmethod


class Property:
    name: str
    type: str
    required: bool = True
    description: str = None

    def __init__(
        self, name: str, type: str, required: bool = True, description: str = None
    ):
        self.name = name
        self.type = type
        self.required = required
        self.description = description


class FunctionCall:
    call_id: str
    name: str
    arguments: dict

    def __init__(self, call_id: str, name: str, arguments: dict = None):
        self.call_id = call_id
        self.name = name
        self.arguments = arguments


class Function:
    name: str
    description: str = None
    parameters: list[Property] = None

    def __init__(
        self, name: str, description: str = None, parameters: list[Property] = None
    ):
        self.name = name
        self.description = description
        self.parameters = parameters

    def to_dict(self):
        if self.parameters is None:
            return {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            }
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {
                    p.name: {"type": p.type, "description": p.description}
                    for p in self.parameters
                },
                "required": [p.name for p in self.parameters if p.required],
            },
        }

    def run(self, function_call: FunctionCall = None):
        if function_call.arguments == {} and self.parameters is not None:
            raise Exception("Missing parameters")
        if function_call.arguments == {} and self.parameters is None:
            return self.function()
        if function_call.arguments != {} and self.parameters is None:
            raise Exception("Unexpected parameters")
        if function_call is not None and self.parameters is not None:
            for p in self.parameters:
                if p.name not in function_call.arguments and p.required:
                    raise Exception(f"Missing parameter {p.name}")
            return self.function(**function_call.arguments)

    def run_catch_exceptions(self, function_call: FunctionCall = None):
        try:
            return self.run(function_call=function_call)
        except Exception as e:
            return str(e)

    @abstractmethod
    def function(self, **kwargs):
        pass
