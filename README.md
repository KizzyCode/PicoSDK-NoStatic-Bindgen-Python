[![License BSD-2-Clause](https://img.shields.io/badge/License-BSD--2--Clause-blue.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![License MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


# `PicoSDK-NoStatic-Bindgen`
Welcome to `PicoSDK-NoStatic-Bindgen` 🎉

This is a helper tool to generate no-`static` no-`inline` wrappers around the public `static inline` functions within
the SDK.

## Word of Warning
We use regex to parse the C headers – so this tool is horribly cursed by definition. It is recommended to cross-check
the generated wrapper.
