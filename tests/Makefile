RST=code_blocks.rst sage_code_blocks.rst images.rst lists.rst math.rst quote.rst tables.rst topics.rst
MD=$(RST:%.rst=%.md) all.md
IPYNB=$(MD:%.md=%.ipynb)
HTML=$(MD:%.md=%.html)
JSON=$(MD:%.md=%.json)

all: $(MD) $(IPYNB)

html: $(HTML)

json: $(JSON)

all.rst: $(RST)
	-rm $@
	for file in $^; do cat $$file >> $@; echo >> $@; done

%.md: %.rst
	pandoc --filter=../sageblockfilter.py $< --atx-headers -o $@

#	sed -i 's/``` {/```{/' $@

%.ipynb: %.md
	notedown --match=fenced $< > $@

%.html: %.ipynb
	ipython nbconvert $< --to html > $@

%.json: %.rst
	pandoc --filter=../sageblockfilter.py $< --atx-headers -o $@

clean:
	-rm *.md *.ipynb *.html
