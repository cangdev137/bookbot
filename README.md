# bookbot

bookbot is a simple personal project inspired by [Boot.dev](https://www.boot.dev).

bookbot can be used to analyze text files and report on the contents. commands generally take the following form:
```
./bookbot.sh [flags] <path_to_text_file>
```

by default, bookbot generates a simple report containing the total word count
and individualized character counts. the simplest possible invocation is: 
```
/bookbot.sh <path_to_text_file>
```

bookbot automatically groups punctuation symbols (any non-alphanumeric characters) into an umbrella "punctuation" term.
to disable this, use the '-v' flag:
```
./bookbot.sh -v <path_to_text_file>
```
