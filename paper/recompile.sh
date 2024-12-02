#latexdiff paper_10_16_2024.tex paper.tex > diff.tex
#~/software/latexdiff/dist/latexdiff-so paper_old.tex paper.tex > diff.tex
#~/software/latexdiff/dist/latexdiff-so paper_old.tex paper.tex > diff.tex
for b in paper; do
#for b in diff; do
#for b in paper diff; do

rm *.aux
rm *.bbl

pdflatex ${b}
bibtex ${b}
pdflatex ${b}
pdflatex ${b}
#dvips -Ppdf ${b}.dvi
#ps2pdf ${b}.ps

#evince ${b}.pdf &

done
