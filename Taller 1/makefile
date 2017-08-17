PUNTO1t = p1table.txt
PUNTO2t = p2table.txt
TO_RM = *.aux *.log

Taller1.pdf : Taller1.tex $(PUNTO1t) $(PUNTO2t) Macro.ijm
	pdflatex $<
	rm $(TO_RM)

$(PUNTO1t) : table.py tracks.csv
	python $^ "Min v [µm/sec]" "Max v [µm/sec]" "Mean v [µm/sec]" "SD v [µm/sec]" > $@

$(PUNTO2t) : table.py count.csv
	python $^ all > $@

clean :
	rm $(TO_RM) *.txt
