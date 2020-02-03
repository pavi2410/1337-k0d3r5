mkdir -p out
for file in *.in; do
    py main.py < "$file" > "out/${file%.in}.out"
done