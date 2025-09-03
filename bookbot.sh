#!/bin/bash
#call the bookbot

verbose=false
while getopts "v" flag; do
    case "${flag}" in 
        v)
            verbose=true
            ;;

        *)
            echo "UNRECOGNIZED FLAG"; >&2
            echo "Usage: $0 [-v] <path_to_txt_file>" >&2
            exit 1
    esac
done

if [[ $verbose == true ]]; then
    verbose_arg="-v"
else
    verbose_arg=""
fi

exec python3 main.py "${verbose_arg}" "${@: -1}"
