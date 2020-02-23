# Donut buddies randomization

How to use:

1. Put a CSV file with two columns (name and family) in the same folder as the script. There can be multiple columns, but these should be the first two, and there shouldn't be duplicate names.
2. Add the name of this CSV to the first line of `Makefile`. It should now read `CSV_IN ?= yourfilename.csv`.
3. In a Terminal/Bash window, type `make` and wait for it to finish running!