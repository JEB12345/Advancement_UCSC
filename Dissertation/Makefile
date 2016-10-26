all: paper

chapters:
	pdflatex Dissertation_chapters.tex
	./bibtool -s -d -x Dissertation_chapters.aux ICRA_2016_SUPERball.bib Dissertation_Doc_Jonathan_Bruce.bib tensegrity_review.bib references.bib > final.bib
	bibtex Dissertation_chapters
	pdflatex Dissertation_chapters.tex
	pdflatex Dissertation_chapters.tex
	-rm *.aux
	-rm *.bbl
	-rm *.blg
	-rm *.out
	-rm *.lot
	-rm *.toc
	-rm *.lof
paper:
	pdflatex Dissertation_Doc_Jonathan_Bruce.tex
	./bibtool -s -d -x Dissertation_Doc_Jonathan_Bruce.aux ICRA_2016_SUPERball.bib Dissertation_Doc_Jonathan_Bruce.bib tensegrity_review.bib references.bib > final.bib
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
