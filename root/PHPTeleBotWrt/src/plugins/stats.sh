#!/bin/sh
# rpcaria=$(uci get aria2.main._rpc_url)
rpcaria="http://127.0.0.1:6800/jsonrpc"

stopped=$(curl "$rpcaria" -H "Content-Type: application/json" -H "Accept: application/json" --data '{"jsonrpc": "2.0","id":"foo", "method": "aria2.getGlobalStat", "params":[]}' | cut -d "{" -f 3 | cut -d "," -f 3 | cut -d ":" -f 2 |tr -d '"')

active=$(curl "$rpcaria" -H "Content-Type: application/json" -H "Accept: application/json" --data '{"jsonrpc": "2.0","id":"foo", "method": "aria2.getGlobalStat", "params":[]}' | cut -d "{" -f 3 | cut -d "," -f 2 | cut -d ":" -f 2 |tr -d '"')

waiting=$(curl "$rpcaria" -H "Content-Type: application/json" -H "Accept: application/json" --data '{"jsonrpc": "2.0","id":"foo", "method": "aria2.getGlobalStat", "params":[]}' | cut -d "{" -f 3 | cut -d "," -f 5 | cut -d ":" -f 2 |tr -d '"')

dspeed=$(curl "$rpcaria" -H "Content-Type: application/json" -H "Accept: application/json" --data '{"jsonrpc": "2.0","id":"foo", "method": "aria2.getGlobalStat", "params":[]}' | cut -d "{" -f 3 | cut -d "," -f 1 | cut -d ":" -f 2 |tr -d '"')
dspeedkb=$(printf '%.0f ' "$((dspeed / 1024))")

echo "Active : ${active}"
echo "Waiting : ${waiting}"
echo "Stopped : ${stopped}"
echo "Speed : ${dspeedkb}KBps"