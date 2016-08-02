git format-patch --minimal --no-prefix --no-stat -U1 --ignore-space-change -o patches start-after-me..HEAD \
&& for i in patches/*.patch; do pygmentize -O full,style=prettydiff -f html -l diff $i | wkhtmltopdf - $i.pdf; done \
&& pdftk patches/*.pdf cat output guide.pdf \
&& rm patches/* \
&& rmdir patches \
&& open guide.pdf
