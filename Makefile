CSV_IN ?= 
CSV_OUT ?= out.csv
WEEKS ?= 15

donuts: donuts.py
	python3 donuts.py $(CSV_IN) $(CSV_OUT) $(WEEKS)

clean:
	rm -f $(CSV_OUT)

.PHONY: clean donuts
