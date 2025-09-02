# bookbot

bookbot is a project inspired by [Boot.dev](https://www.boot.dev).

bookbot can be used to analyze text files and report on the contents. commands generally take the form
```python3 main.py [flags] <path_to_text_file>```

by default, bookbot generates a simple report containing the total word count
and individualized character counts. the simplest possible invocation is: 
```python3 main.py <path_to_text_file>```

bookbot automatically groups punctuation symbols (any non-alphanumeric characters) into an umbrella "punctuation" term.
to disable this, use the *'-v'* flag:
```python3 main.py -v <path_to_text_file>```


