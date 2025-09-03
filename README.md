# bookbot

bookbot is a simple personal project inspired by [Boot.dev](https://www.boot.dev).

bookbot can be used to analyze text files and report on the contents. commands generally take the following form:
```
./bookbot.sh [flags] book.txt
```

by default, bookbot generates a simple report containing the total word count
and individualized character counts. the simplest possible invocation is: 
```
/bookbot.sh book.txt
```

bookbot automatically groups punctuation symbols (any non-alphanumeric characters) into an umbrella "punctuation" term.
to disable this, use the '-v' flag:
```
./bookbot.sh -v book.txt
```

sometimes, there are many unique alphanumeric characters.
this can make the character count portion of the report lengthy. 
the '-n' flag can be used to truncate the character count section to display only the top *n* most common characters.
For example, the following truncates the character counts to only display the top 10 characters:
```
./bookbot.sh -n 10 book.txt
```


