#!/bin/bash
if [ "$1" != "" ]; then
	python generate_mistake.py $1 | python suggestion.py $1 | grep "NO SUGGESTION"
else
	echo No word dictionary file given.
fi
echo Done.