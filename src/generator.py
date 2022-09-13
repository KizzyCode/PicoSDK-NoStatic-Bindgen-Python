from parser import Header, Function


class Function:
    """A wrapper for a `static inline` function"""

    synthesized: str
    """The synthesized wrapper"""

    def __init__(self, function: Function, prefix: str, suffix: str) -> None:
        # Prepare arguments
        typed_args = Function._typed_arguments(function.arguments)
        untyped_args = Function._untyped_arguments(function.arguments)

        # Synthesize function
        self.synthesized = function.comment + "\n"
        self.synthesized += f"{ function.rettype } { prefix }{ function.name }{ suffix }({ typed_args }) {{\n"
        self.synthesized += f"    return { function.name }({ untyped_args });\n"
        self.synthesized += f"}}"
        
    def _typed_arguments(arglist: list[tuple[str, str]]) -> str:
        """Creates a typed argument string from an arglist"""
        typed_args = map(lambda arg: f"{ arg[0] } { arg[1] }", arglist)
        return ", ".join(typed_args)
    
    def _untyped_arguments(arglist: list[tuple[str, str]]) -> str:
        """Creates an untyped argument string from an arglist"""
        untyped_args = map(lambda arg: arg[1], arglist)
        return ", ".join(untyped_args)


class Wrapper:
    """A wrapper file"""

    synthesized: str
    """The synthesized source code"""

    def __init__(self, headers: list[Header], functions: list[Function]) -> None:
        self.synthesized = ""

        # Include all the headers
        for header in headers:
            if len(header.functions) > 0:
                self.synthesized += f"#include \"{ header.include_name }\"\n"
        self.synthesized += "\n\n"

        # Insert the functinos
        for function in functions:
            self.synthesized += f"{ function.synthesized }\n\n\n"
