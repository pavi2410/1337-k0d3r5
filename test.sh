files="$1*.in"
for file in $files; do
    echo -FILENAME-----------
    echo $file
    echo -INPUT--------------
    cat $file
    echo -OUTPUT-------------
    py main.py < "$file"
    echo --------------------
done