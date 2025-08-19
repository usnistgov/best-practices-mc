#latexdiff paperv1.0.tex paperv1.1.tex > diffv1.1.tex
for b in paperv1.1; do
#for b in diffv1.1; do
#for b in paperv1.0 diffv1.0; do

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
