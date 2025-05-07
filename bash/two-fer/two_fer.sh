#!/usr/bin/env bash



   main () {
        if [[ -n $1 ]]; then
        # If a name is provided, use it
        echo "One for $1, one for me."
        else
        # If no name is provided, use "you" by default
        echo "One for you, one for me."
    fi
}
   

  main "$@"


