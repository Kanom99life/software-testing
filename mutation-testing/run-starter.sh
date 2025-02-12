mutation_killed=0
# total_mutations=0

#====Complete the code below
rm -rf __pycache__ .pytest_cache mutation_*.py
python ./mutator-starter.py ./sample_program.py

cp sample_program.py sample_program_backup.py

count_mutations=$(ls mutation_*.py | wc -l)
total_mutations=$count_mutations
for i in $( seq 1 $count_mutations );
# for i in {1..15};
do
    cp mutation_$i.py sample_program.py
    # total_mutations=$((total_mutations+1))
    pytest --cache-clear -v || mutation_killed=$((mutation_killed+1))
done

mv sample_program_backup.py sample_program.py






#====end of your code

mutation_score=$(echo "scale=2; $mutation_killed / $total_mutations" | bc)
echo "Mutation score: $mutation_score"