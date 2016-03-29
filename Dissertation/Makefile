all: paper

paper:
	pdflatex Dissertation_Doc_Jonathan_Bruce.tex
	bibtex Dissertation_Doc_Jonathan_Bruce
	pdflatex Dissertation_Doc_Jonathan_Bruce.tex
	pdflatex Dissertation_Doc_Jonathan_Bruce.tex
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
	-rm Dissertation_Doc_Jonathan_Bruce.pdf
	-rm Dissertation_Doc_Jonathan_Bruce.dvi
	-rm Dissertation_Doc_Jonathan_Bruce.ps
	-rm *.blg
	-rm img/*esp-converted-to.pdf
	-rm *~ 
