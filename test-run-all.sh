#!/bin/bash

function perror()
{
    echo "!! Failed: $1"
    exit $2
}

function clean-up()
{
	rm -f *.pyc && echo "performed clean-up"	
}


clean-up
for item in `ls *-ut.py`; do
    echo "run: $item"
    python $item &> /dev/null || perror "Failed running test: $item"; 
    echo "test: $item passed"
done

clean-up

exit 0