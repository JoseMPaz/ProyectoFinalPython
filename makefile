# Nombre base del archivo (sin extensión)
TEXFILE=informe

# Regla por defecto
all: $(TEXFILE).pdf

# Compilar el archivo PDF
$(TEXFILE).pdf: $(TEXFILE).tex
	pdflatex -shell-escape $(TEXFILE).tex
	pdflatex -shell-escape $(TEXFILE).tex

# Limpieza de archivos auxiliares
clean:
	rm -f $(TEXFILE).aux $(TEXFILE).log $(TEXFILE).toc $(TEXFILE).out $(TEXFILE).lof $(TEXFILE).lot

# Limpiar todo, incluyendo el PDF
cleanall: clean
	rm -f $(TEXFILE).pdf
