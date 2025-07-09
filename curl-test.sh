#!/bin/bash

INITIAL_GET="$(curl -s http://localhost:5000/app/timeline_post | jq '.timeline_posts | length')"
if [ -z "$INITIAL_GET" ]; then
    echo "Initial GET request failed"
    exit 1
else
    echo "Initial GET request was successful"
fi
echo "Number of timeline posts before POST: ${INITIAL_GET}"
curl -X POST -s http://localhost:5000/app/timeline_post -d \
"name=Pavlo Kostianov&email=kostianp@tcd.ie&content=Testing my endpoints. Random number - ${RANDOM}."
if [ $? -eq 0 ]; then
    echo "POST request was successful"
else
    echo "POST request failed"
    exit 1
fi
FINAL_GET="$(curl -s http://localhost:5000/app/timeline_post | jq '.timeline_posts | length')"
if [ "$FINAL_GET" -gt "$INITIAL_GET" ]; then
    echo "Final GET request confirms that the post have been added. It's now ${FINAL_GET} posts."
else
    echo "GET request shows that the post was not added. There is an issue with POST request."
fi
curl -X DELETE http://localhost:5000/app/timeline_post