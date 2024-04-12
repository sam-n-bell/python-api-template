NAME=$1
python project_setup.py "$NAME" "0"
cd ../$NAME
find . -type f \( -name "*.yaml" -o -name "*.py" -o -name "*.example" \) -exec sed -i "s/{{template_name}}/\L$NAME/g" {} +
find . -type f \( -name "*.md" \) -exec sed -i "s/{{YourAppName}}/\L$NAME/g" {} +
cp .env.example .env
rm -r -f .git
rm -r -f .idea
echo "New project directory $NAME created. Start coding. Window closes in 8 seconds."
sleep 8