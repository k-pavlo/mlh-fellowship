#!/bin/bash

# Send initial GET request and calculate number of timeline posts to compare later
INITIAL_GET="$(curl -s http://localhost:5000/app/timeline_post | jq '.timeline_posts | length')"

# If variable is null, then curl failed.
if [ -z "$INITIAL_GET" ]; then
    echo "Initial GET request failed"
    exit 1
else
    echo "Initial GET request was successful"
fi

echo "Number of timeline posts before POST: ${INITIAL_GET}"

# Do POST request and check if curl was successful
curl -X POST -s http://localhost:5000/app/timeline_post -d \
"name=Pavlo Kostianov&email=kostianp@tcd.ie&content=Testing my endpoints. Random number - ${RANDOM}."
if [ $? -eq 0 ]; then
    echo "POST request was successful"
else
    echo "POST request failed"
    exit 1
fi

# Make final GET request, count amount of posts.
FINAL_GET="$(curl -s http://localhost:5000/app/timeline_post | jq '.timeline_posts | length')"

# Compare final amount to the initial amount of posts 
# to see if it has been increased to confirm the post was added.
if [ "$FINAL_GET" -gt "$INITIAL_GET" ]; then
    echo "Final GET request confirms that the post have been added. It's now ${FINAL_GET} posts."
else
    echo "GET request shows that the post was not added. There is an issue with POST request."
fi

# Delete the test timeline post (last post)
curl -X DELETE http://localhost:5000/app/timeline_post