entry_nums=(
  '2022XY59876'
  '2022XY59877'
  '2022XY59878'
  '2022XY59879'
  '2021ME11021'
)

mkdir -p logs

for i in ${entry_nums[@]}; do
  if [[ -e "${i}_assignment_4.py" ]]; then
    (python3 test_script_ass4.py "${i}_assignment_4.py" > "logs/${i}.log") || true
  else
    echo "File ${i}_assignment_4.py not found" > "logs/${i}.log"
  fi  
done