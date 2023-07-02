NAME=$1

find . -type f \( -name "*.yaml" -o -name "*.py" \) -exec sed -i "s/{{template_name}}/\L$NAME/g" {} +

and rm *-e

