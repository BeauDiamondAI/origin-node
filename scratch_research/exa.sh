#!/bin/bash
EXA_KEY=$(grep '^EXA_API_KEY=' .env | cut -d= -f2- | tr -d '"'"'"'[:space:]')
Q="$1"
curl -s -X POST https://api.exa.ai/search \
  -H "x-api-key: $EXA_KEY" -H "Content-Type: application/json" \
  -d "{\"query\": $(python3 -c "import json,sys; print(json.dumps(sys.argv[1]))" "$Q"), \"type\":\"deep-reasoning\", \"numResults\":8, \"contents\":{\"summary\":true}}" \
  | python3 -c "import json,sys; d=json.load(sys.stdin); [print('###', r.get('title'),'\n',r.get('url'),'\n',(r.get('summary') or '')[:900],'\n') for r in d.get('results',[])]"
