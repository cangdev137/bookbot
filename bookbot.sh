#!/bin/bash
#call the bookbot

verbose=false
verbose_arg=""

truncated=false
truncated_arg=""
max_lines_arg=""

file=""

for arg in "$@"; do
    #if -n flag is found, get number of lines to truncate to make it an argument suitable for the python file
    if $truncated; then
        truncated_arg="-n";
        if [[ "$arg" =~ ^[0-9]+$ ]]; then
            max_lines_arg=$arg
        else
            echo "Error: -n provided without a positive number, got $arg" >&2
            echo "Example Usage: ./bookbot.sh -n 10 book.txt" >&2
            exit 1
        fi
        #don't allow this if block to execute again
        truncated=false;
        continue;
    fi
        
    case "$arg" in 
        "-v")
            verbose=true
            verbose_arg=$arg
            continue
            ;;
            
        "-n")
            truncated=true
            truncated_arg="-n"
            continue
            ;;
        -*)
            echo "UNRECOGNIZED FLAG" >&2;
            echo "Usage: $0 [flag] <path_to_txt_file>" >&2;
            exit 1;
            ;;
        *)
            if [ -z "$file" ]; then
                file="$arg";
            else
                echo "Too many arguments" >&2;
                echo "Usage: $0 [flag] <path_to_txt_file>" >&2;
                exit 1
            fi
            ;;
    esac
done

exec python3 ./src/main.py "${verbose_arg}" "${truncated_arg}" "${max_lines_arg}" "$file"
