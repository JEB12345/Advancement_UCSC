all: paper

paper:
	pdflatex Advancement_Doc_Jonathan_Bruce.tex
	bibtex Advancement_Doc_Jonathan_Bruce
	pdflatex Advancement_Doc_Jonathan_Bruce.tex
	pdflatex Advancement_Doc_Jonathan_Bruce.tex
	-rm *.aux
	-rm *.bbl
	-rm *.blg
	-rm *.out
	-rm *.lot
	-rm *.toc
	-rm *.lof

clean:
	-rm *.aux
	-rm *.log
	-rm *.bbl
	-rm Advancement_Doc_Jonathan_Bruce.pdf
	-rm Advancement_Doc_Jonathan_Bruce.dvi
	-rm Advancement_Doc_Jonathan_Bruce.ps
	-rm *.blg
	-rm img/*esp-converted-to.pdf
	-rm *~ 
