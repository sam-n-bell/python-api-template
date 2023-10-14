NAME=$1
python project_setup.py "$NAME"
cd ..
cd $NAME
find . -type f \( -name "*.yaml" -o -name "*.py" \) -exec sed -i "s/{{template_name}}/\L$NAME/g" {} +
find . -type f \( -name "*.md" \) -exec sed -i "s/{{YourAppName}}/\L$NAME/g" {} +
echo "Start coding"
sleep 5
