# emojpy - Having Fun With Emojis
Emoji To Python Transpiler - Having Fun With Emojis

# proposal
The idea behind emojpy is to build a valid transpiler for code expressed trough emojis. It supports 3.6+ python.

## example
Basic Python Example:

```py
a = 'Hello World'
print(a)
```

Emojpy Script
```py
🔑😜
😜 = 'Hello World'
📣(😜)
```

## dialects
From beginning emojpy contains the possibility to define you own emojpy-dialect. 

## file extension
Default file extension for emojpy files is .💎

> Note: In future Versions this will be changebale in the dialect file

## unicode support
This transpiler supports emojis expressed trough unicode. An example of unicode emojis you can find [here](https://unicode.org/emoji/charts/full-emoji-list.html).

## working samples
Under examples you will find some very simple working examples. Learn how to execute them with the parsing script in [Examples Doc](./doc/example.md).

# release plan
Features For Release Version 1.0

[ ] Transpiler from emojpy to python*<br> 
[ ] Transpiler from python to emojpy*<br>
[ ] Draft for dialect files*<br>

*\*supporting all 35 python [keywords](https://docs.python.org/3.7/reference/lexical_analysis.html#keywords), numbers and variable declaration*
