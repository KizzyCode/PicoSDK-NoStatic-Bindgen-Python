import re


class Function:
    """A `static inline` function"""

    comment: str
    """The function doc-comment"""
    name: str
    """The function name"""
    arguments: list[tuple[str, str]]
    """The function arguments"""
    rettype: str
    """The function return type"""

    def __init__(self, comment: str, signature: str) -> None:
        # Parse the function
        [rettype, name, arglist] = Function._parse_signature_outer(signature)
        arguments = Function._parse_signature_inner(arglist)
        
        # Init self
        self.comment = comment
        self.name = name
        self.arguments = arguments
        self.rettype = rettype

    def _parse_signature_outer(signature: str) -> tuple[str, str, str]:
        """Parse the outer function signature"""

        # Split the signature into return type, name and argument list
        regex = re.compile(r"static\s+inline\s+(.*?)\s+(\w*)\s*\((.*?)\)", flags=re.S)
        match = regex.fullmatch(signature)
        return (match.group(1).strip(), match.group(2).strip(), match.group(3).strip())
    
    def _parse_signature_inner(arglist: str) -> list[tuple[str, str]]:
        """Parses the inner function signature"""

        # Treat the arguments as some weird kind of CSV
        regex = re.compile(r"(.+[\s\*])(\w+)", flags=re.S)
        parsed = []
        for arg in map(lambda arg: arg.strip(), arglist.split(",")):
            # Ignore void arguments
            if arg != "void":
                # Split the argument into type and name
                match = regex.fullmatch(arg)
                parsed.append((match.group(1).strip(), match.group(2).strip()))
        return parsed


class Header:
    """A header file"""
    
    functions: list[Function]
    """The `static inline` functions within the source file"""

    include_name: str
    """The include name for the header file"""

    def __init__(self, path: str) -> None:
        # Read the file
        with open(path, "r") as header:
            sourcecode = header.read()

        # Init self
        self.functions = Header._parse_functions(sourcecode)
        self.include_name = Header._get_include_name(path)

    def _parse_functions(sourcecode: str) -> list[Function]:
        """Parses all `static inline` functions"""

        # Split the function into the doccomment part and the function signature
        regex = re.compile(r"(\/\*\![^\n]*\n(?:\s+\*[^\n]*\n)*)\s*(static\s+inline.*?\(.*?\))\s+{", flags=re.S)
        functions = []
        for match in regex.finditer(sourcecode):
            # Get the doc-comment and the signature
            function = Function(match.group(1).strip(), match.group(2).strip())
            functions.append(function)
        return functions

    def _get_include_name(path: str) -> str:
        """Gets the appropriate name for `#include "<name>"`-statements"""
        regex = re.compile(r".*/include/(.*\.h)")
        match = regex.fullmatch(path)
        return match.group(1).strip()