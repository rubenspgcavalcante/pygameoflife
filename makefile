# -- Macros -- #
FLAGS = -m compileall .
CURRENT_DIR = ${PWD##*/}
CX_FREEZE_VER = 4.3.1
CX_FREEZE_LINK = "http://downloads.sourceforge.net/project/cx-freeze/$(CX_FREEZE_VER)/cx_Freeze-$(CX_FREEZE_VER).tar.gz"
EXCLUDE_MODULES = tcl,ttk,Tkinter,setuptolls,numpy
APT_DEPENDECES= gcc python python-dev python-imaging python-pygame python-qt4 pyqt4-dev-tools zip

OS_TYPE = $(shell if [ `uname` = Linux ] ; then echo Linux ; else echo Win ; fi)

ARCH_TYPE = $(shell if [ `uname -p` != unknown ] ; then uname -p ; else uname -m ; fi)

BIN_NAME = $(shell if [ `uname` = Linux ] ; then echo run-pygameoflife ; else echo run-pygameoflife.exe ; fi)

HIDE_CONSOLE_WIN32 = $(shell if [ `uname` != Linux ] ; then echo --base-name=Win32GUI ; fi)

.PHONY: resources

# -- Rules -- #
all: build clean

build: resources
	python $(FLAGS)
	mkdir -p build
	cp --parents ./*.pyc build/
	cp --parents ./models/*.pyc build/
	cp --parents ./views/*.pyc build/
	cp --parents ./controllers/*.pyc build/
	cp --parents ./helpers/*.pyc build/
	cp --parents ./resources/*.pyc build/

	mkdir -p freezed
	mkdir -p freezed/pygameoflife
	cxfreeze __main__.py $(HIDE_CONSOLE_WIN32) --target-dir freezed/pygameoflife --target-name $(BIN_NAME) --exclude-modules=$(EXCLUDE_MODULES)

	cp --parents ./resources/cache/*.png freezed/pygameoflife/
	cp --parents ./resources/static/*.png freezed/pygameoflife/

	rm -f releases/pygame-of-life_$(OS_TYPE)_$(ARCH_TYPE).zip
	cd freezed && zip -9urT ../releases/pygame-of-life_$(OS_TYPE)_$(ARCH_TYPE) * && cd ..

resources:
	#Generating game images and qt resources
	pyrcc4 -py2 resources/qt/resources.qrc -o resources/qtresources.py
	pyuic4 resources/qt/launcher.ui -o resources/qtlauncher.py
	python __main__.py genimg

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm build/ -rf
	rm freezed/ -rf
	rm cx_Freeze-* -rf

install: isroot
	cp releases/pygame-of-life_$(OS_TYPE)_$(ARCH_TYPE).zip /usr/share/
	unzip -uo /usr/share/pygame-of-life_$(OS_TYPE)_$(ARCH_TYPE).zip -d /usr/share
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
	apt-get update --fix-missing
	apt-get install $(APT_DEPENDECES)
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