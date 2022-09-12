[![License BSD-2-Clause](https://img.shields.io/badge/License-BSD--2--Clause-blue.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![License MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


# `PicoSDK-NoStatic-Bindgen`
Welcome to `PicoSDK-NoStatic-Bindgen` 🎉

This is a helper tool to generate no-`static` no-`inline` wrappers around the public `static inline` functions within
the SDK.

## Word of Warning
We use regex to parse the C headers – so this tool is horribly cursed by definition. It is recommended to cross-check
the generated wrapper.

## Quickstart
1. Clone the repo: `git clone https://github.com/KizzyCode/PicoSDK-NoStatic-Bindgen-Python`
2. Enter the repo: `cd PicoSDK-NoStatic-Bindgen-Python`
3. Checkout the SDK subrepo: `git submodule update --init`
4. Generate the wrappers: `python3 src`
