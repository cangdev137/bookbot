# bookbot

bookbot is a simple personal project inspired by [Boot.dev](https://www.boot.dev).

to try the tool out, install the source code and bash script using the following commands:
```
git clone git@github.com:cangdev137/bookbot.git && cd bookbot
```

bookbot allows you to analyze a text file and generates a report on the total word count, line count, and individualized character counts.
to generate the default report, run the following command:
```
./bookbot.sh book.txt
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


