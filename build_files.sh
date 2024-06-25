echo "BUILD START"
python-3.12.1 -m pip install -r requirment.txt
ppython-3.12.1 manage.py collectstatic --noinput --clear
echo "BUILD END"