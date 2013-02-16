# -- Macros -- #
FLAGS = -m compileall .
CURRENT_DIR = ${PWD##*/}
CX_FREEZE_VER = 4.3.1
CX_FREEZE_LINK = "http://downloads.sourceforge.net/project/cx-freeze/$(CX_FREEZE_VER)/cx_Freeze-$(CX_FREEZE_VER).tar.gz"

OS_TYPE = $(shell uname)
ARCH_TYPE = $(shell uname -p)

# -- Rules -- #
all: build clean

build:
	python $(FLAGS)
	python __main__.py genimg
	mkdir -p build
	cp --parents ./*.pyc build/
	cp --parents ./models/*.pyc build/
	cp --parents ./views/*.pyc build/
	cp --parents ./controllers/*.pyc build/
	cp --parents ./helpers/*.pyc build/
	cp --parents ./resources/*.pyc build/

	mkdir -p freezed
	cxfreeze __main__.py --target-dir freezed --target-name run-pygameoflife --exclude-modules=tcl,ttk,Tkinter

	cp --parents ./resources/cache/*.png freezed/
	cp --parents ./resources/static/*.png freezed/
	cp --parents ./resources/qt/*.ui freezed/

	cd freezed && zip -9urT ../releases/pygame-of-life_$(OS_TYPE)_$(ARCH_TYPE) * && cd ..

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm build/ -rf
	rm freezed/ -rf
	rm cx_Freeze-* -rf

install: isroot
	cp releases/pygame-of-life_$(OS_TYPE)_$(ARCH_TYPE).zip /usr/share/
	unzip -uo /usr/share/pygame-of-life_$(OS_TYPE)_$(ARCH_TYPE).zip -d /usr/share/pygameoflife
	rm -f /usr/share/pygame-of-life_$(OS_TYPE)_$(ARCH_TYPE).zip
	cp resources/static/icon.png /usr/share/pygameoflife/
	cp pygameoflife.desktop /usr/share/applications/
	ln -s --force /usr/share/pygameoflife/run-pygameoflife /usr/games/pygameoflife 
	chmod +x /usr/games/pygameoflife

uninstall: isroot
	rm -rf /usr/share/pygameoflife
	rm -f /usr/games/pygameoflife
	rm -f /usr/share/applications/pygameoflife.desktop

setup: isroot
	#Dowload and install dependeces
	apt-get install gcc python python-dev python-pygame python-qt4 zip
	wget $(CX_FREEZE_LINK) -t 5 -S -w 1 -N --trust-server-name
	tar -zxvf cx_Freeze-$(CX_FREEZE_VER).tar.gz --overwrite
	cd cx_Freeze-$(CX_FREEZE_VER) && python setup.py install
	rm -rf cx_Freeze-$(CX_FREEZE_VER) cx_Freeze-$(CX_FREEZE_VER).tar.gz build

isroot:
	@export USER=`whoami`
	@if [ "$(USER)" != "root" ]; then \
		echo "ERROR: Requires being root or sudo permissions" ; \
	    exit 1 ; \
	fi

print:
	cd freezed && zip -9urT ../releases/pygame-of-life_$(OS_TYPE)_$(ARCH_TYPE) * && cd ..
