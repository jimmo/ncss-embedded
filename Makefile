VPATH = chapters
CHAPTERS = 1-intro.md 2-intro-microbit.md 3-intro-electronics.md 4-states-classes.md 5-grove-pwm-servos.md 6-radio-files-plotting.md 7-bitbot-neopixels.md 8-filtering-control.md 9-advanced-components.md 10-pyboard-quokka.md 11-learn-more.md 12-lab-exercises.md
TEX_CHAPTERS = $(CHAPTERS:md=tex)

.PHONY: all clean

all: notes.pdf

clean:
	rm -f $(TEX_CHAPTERS)
	rm -f notes.pdf

%.tex : %.md 
	pandoc -o $@ $<

notes.pdf: notes.tex $(TEX_CHAPTERS)
	xelatex notes
	xelatex notes
	makeindex notes
	xelatex notes

