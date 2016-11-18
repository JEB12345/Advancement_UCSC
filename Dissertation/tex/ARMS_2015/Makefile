all: paper

paper:
	pdflatex TwoTierMonteCarloTensegrity.tex
	bibtex TwoTierMonteCarloTensegrity
	pdflatex TwoTierMonteCarloTensegrity.tex
	pdflatex TwoTierMonteCarloTensegrity.tex
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
	-rm TwoTierMonteCarloTensegrity.pdf
	-rm TwoTierMonteCarloTensegrity.dvi
	-rm TwoTierMonteCarloTensegrity.ps
	-rm *.blg
	-rm ../Pictures/*esp-converted-to.pdf
	-rm *~ 
