echo "BUILD START"
python3.12.1 -m pip install -r requirment.txt
ppython3.12.1 manage.py collectstatic --noinput --clear
echo "BUILD END"