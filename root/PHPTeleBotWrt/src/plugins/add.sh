#!/bin/sh
URL="$1"
if [ -z $URL]; then
    printf "Please retry with valid url\nExample : /aria2add <code>http://site.com/file.mp4</code>"

else
    curl http://127.0.0.1:6800/jsonrpc -X POST --data '{"jsonrpc": "2.0","id":"foo", "method": "aria2.addUri", "params":[["'"$URL"'"]]}'
    printf "Task added to Aria2 - Check download status /aria2stats"
fi
