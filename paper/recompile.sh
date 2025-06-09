latexdiff paperv0.1.tex paperv1.0.tex > diffv1.0.tex
#for b in paperv1.0; do
#for b in diffv1.0; do
for b in paperv1.0 diffv1.0; do

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
