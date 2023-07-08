NAME=$1

find . -type f \( -name "*.yaml" -o -name "*.py" \) -exec sed -i "s/{{template_name}}/\L$NAME/g" {} +
find . -type f \( -name "*.md" \) -exec sed -i "s/{{YourAppName}}/\L$NAME/g" {} +

and rm *-e

