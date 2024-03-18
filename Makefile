CXXFLAGS = -O2

plot: farey_diff.txt plot.py
	cat farey_diff.txt | python plot.py

farey_diff.txt: farey_diff
	./farey_diff > $@

farey_diff: farey_diff.cpp
