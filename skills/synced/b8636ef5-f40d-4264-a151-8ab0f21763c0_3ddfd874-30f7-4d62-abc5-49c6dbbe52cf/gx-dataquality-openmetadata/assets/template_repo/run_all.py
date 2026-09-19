"""
run_all.py -- the single command that runs every table under config/tables/.

Usage:
    python run_all.py                                                          # every table
    python run_all.py config/tables/scm.sipscmdb_prod.client_partnership.yaml  # just one

Setup (first time only):
    pip install -r requirements.txt
    cp .env.example .env      # then fill in real values in .env

Safe to re-run any time -- each table's Test Cases are created once and
reused after that; every run just adds a fresh result on top of them.

Adding a new table to test later needs no new Python: drop a new
config/tables/<source>.<schema>.<table>.yaml file (copy an existing one as a
template) and run this again.
"""
import sys

from dotenv import load_dotenv
load_dotenv()

from src.runner import run_all, run_table

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_table(sys.argv[1])
    else:
        run_all()
