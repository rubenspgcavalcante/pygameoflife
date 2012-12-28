# -- Macros -- #
FLAGS = -m compileall .
CURRENT_DIR = ${PWD##*/}

# -- Rules -- #
all: build clean

build:
	python $(FLAGS)
	mkdir -p build
	cp --parents ./*.pyc build/
	cp --parents ./models/*.pyc build/
	cp --parents ./views/*.pyc build/
	cp --parents ./controllers/*.pyc build/
	cp --parents ./helpers/*.pyc build/
	cp --parents ./resources/*.pyc build/
	cp --parents ./resources/data/*.png build/

	cd build/ && zip -r9 ../pygame-of-life * && cd ..

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm build/ -rf

install: isroot
	mkdir -p /usr/share/pygameoflife 
	cp game-of-life.zip /usr/share/pygameoflife/ 
	echo "python pygame-of-life.zip run" >> /usr/share/pygameoflife/run.sh 
	ln -s --force /usr/share/pygameoflife/run.sh /usr/games/pygameoflife 
	chmod +x /usr/games/pygameoflife

uninstall: isroot
	rm -rf /usr/share/pygameoflife
	rm -f /usr/games/pygameoflife

setup: isroot
	#Dowload dependeces
	apt-get install python python-pygame zip

isroot:
	@export USER=`whoami`
	@if [ "$(USER)" != "root" ]; then \
		echo "ERROR: Requires being root or sudo permissions" ; \
	    exit 1 ; \
	fi