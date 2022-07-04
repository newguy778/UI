#bin/env/zsh

URL="http://127.0.0.1:8000"



curl -w " = Home\n" "$URL"

curl -w "\n" "$URL/fake/lastname"

curl -w "\n" "$URL/fake/firstname"