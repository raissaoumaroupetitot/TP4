import os
import sys
os.system("git bisect start " +sys.argv[1] + " e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")
os.system("git bisect run python3.9 manage.py test")