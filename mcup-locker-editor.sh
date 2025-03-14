#!/bin/bash

LOCKER_TOOL_SCRIPT="src/locker_tool.py"

if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed."
    exit 1
fi

if [ ! -f "$LOCKER_TOOL_SCRIPT" ]; then
    echo "Error: locker_tool.py not found at $LOCKER_TOOL_SCRIPT"
    exit 1
fi

python3 "$LOCKER_TOOL_SCRIPT" "$@"