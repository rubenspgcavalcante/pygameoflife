# -- Macros -- #

FLAGS = -m compileall .
CURRENT_DIR = ${PWD##*/}
CX_FREEZE_VER = 4.3.1
CX_FREEZE_LINK = "http://downloads.sourceforge.net/project/cx-freeze/$(CX_FREEZE_VER)/cx_Freeze-$(CX_FREEZE_VER).tar.gz"
EXCLUDE_MODULES = tcl,ttk,Tkinter,setuptolls,numpy
APT_DEPENDECES= gcc python python-dev python-imaging python-pygame python-qt4 pyqt4-dev-tools zip
HIDE_CONSOLE_WIN32 = $(shell if [ `uname` != Linux ] ; then echo --base-name=Win32GUI ; fi)

# --------------------------------------- Game attributes ----------------------------------------------------#
OS_TYPE = $(shell if [ `uname` = Linux ] ; then echo Linux ; else echo Win ; fi)
ARCH_TYPE = $(shell if [ `uname -p` != unknown ] ; then uname -p ; else uname -m ; fi)
BIN_NAME = $(shell if [ `uname` = Linux ] ; then echo run-$(GAME_NAME) ; else echo run-$(GAME_NAME).exe ; fi)
GAME_VERSION = $(shell python __main__.py --version)
GAME_NAME = pygameoflife
ZIP_NAME = $(GAME_NAME)_$(GAME_VERSION)_$(OS_TYPE)_$(ARCH_TYPE)
# ------------------------------------- End game attributes --------------------------------------------------#

.PHONY: resources

# -- Rules -- #
all: build clean

teste:
	echo $(GAME_VERSION)

build: resources
	python $(FLAGS)
	mkdir -p build
	cp --parents ./*.pyc build/
	cp --parents ./models/*.pyc build/
	cp --parents ./views/*.pyc build/
	cp --parents ./controllers/*.pyc build/
	cp --parents ./helpers/*.pyc build/

	mkdir -p freezed
	mkdir -p freezed/$(GAME_NAME)
	cxfreeze __main__.py $(HIDE_CONSOLE_WIN32) --target-dir freezed/$(GAME_NAME) --target-name $(BIN_NAME) --exclude-modules=$(EXCLUDE_MODULES)

	cp --parents ./resources/cache/*.png freezed/$(GAME_NAME)/
	cp --parents ./resources/static/*.png freezed/$(GAME_NAME)/

	rm -f releases/$(ZIP_NAME).zip
	cd freezed && zip -9urT ../releases/$(ZIP_NAME).zip * && cd ..

resources:
	#Generating game images and qt resources
	pyrcc4 -py2 resources/qt/resources.qrc -o helpers/qtresources.py
	pyuic4 resources/qt/launcher.ui -o views/qtlauncher.py
	python __main__.py genimg

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm build/ -rf
	rm freezed/ -rf
	rm cx_Freeze-* -rf
	rm *~ -rf

install: isroot
	cp releases/$(ZIP_NAME).zip /usr/share/
	unzip -uo /usr/share/$(ZIP_NAME).zip -d /usr/share
	rm -f /usr/share/$(ZIP_NAME).zip
	cp resources/static/icon.png /usr/share/$(GAME_NAME)/
	cp $(GAME_NAME).desktop /usr/share/applications/
	ln -s --force /usr/share/$(GAME_NAME)/run-$(GAME_NAME) /usr/games/$(GAME_NAME) 
	chmod +x /usr/games/$(GAME_NAME)

uninstall: isroot
	rm -rf /usr/share/$(GAME_NAME)
	rm -f /usr/games/$(GAME_NAME)
	rm -f /usr/share/applications/$(GAME_NAME).desktop

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
