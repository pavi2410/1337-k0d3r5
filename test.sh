echo Testing...
for file in *.in; do
    echo -e "\n"
    echo -FILENAME-----------
    echo $file
    echo -INPUT--------------
    cat $file
    echo -OUTPUT-------------
    py main.py < "$file"
    echo --------------------
done