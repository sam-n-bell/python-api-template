NAME=Pflugerville

sed -i -e 's/{{template}}/$NAME/g' *.py

and rm *-e