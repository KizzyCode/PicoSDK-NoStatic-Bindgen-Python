#!/usr/bin/env python3

from glob import glob
from os import environ
from parser import Header
from generator import Function, Wrapper


if __name__ == "__main__":
    # Use custom prefix if specified
    prefix = environ.get("PREFIX", "nostatic_")

    # Collect all headers
    header_paths = glob("pico-sdk/src/common/**/include/**/*.h", recursive=True)
    header_paths += glob("pico-sdk/src/rp2_common/**/include/**/*.h", recursive=True)
    header_paths += glob("pico-sdk/src/rp2040/**/include/**/*.h", recursive=True)
    headers = list(map(lambda path: Header(path), header_paths))

    # Create the wrappers
    wrappers = []
    for header in headers:
        for function in header.functions:
            wrapper = Function(function, prefix)
            wrappers.append(wrapper)
    
    # Create the wrapper file
    wrapper_file = Wrapper(headers, wrappers)
    print(wrapper_file.synthesized)
