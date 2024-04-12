#!/bin/bash

NAME=$1
python3 project_setup.py "$NAME" "1"
cd ../$NAME
echo $PWD

find . -type f \( -name "*.yaml" -o -name "*.py" -o -name "*.example" -o -name "Makefile" \) -exec sed -i '' "s/{{template_name}}/$NAME/g" {} +
find . -type f \( -name "*.md" \) -exec sed -i '' "s/{{YourAppName}}/$NAME/g" {} +
rm -r -f .git
rm -r -f .idea
cp .env.example .env
echo "New project directory $NAME created. Start coding. Window closes in 8 seconds."
sleep 8