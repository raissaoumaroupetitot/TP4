import os
os.system("git bisect start $badhash $goodhash")
os.system("git bisect run python3.9 manage.py test")