NAME=$1
python project_setup.py "$NAME"
cd ../$NAME
find . -type f \( -name "*.yaml" -o -name "*.py" \) -exec sed -i "s/{{template_name}}/\L$NAME/g" {} +
find . -type f \( -name "*.md" \) -exec sed -i "s/{{YourAppName}}/\L$NAME/g" {} +
echo "New project directory $NAME created. Start coding."
sleep 5
