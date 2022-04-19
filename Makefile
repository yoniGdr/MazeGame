setup: requirements.txt 
	@pip3 install -r requirements.txt

clean: 
	@rm -rf src/__pycache__ *.pyc
	@rm -rf src/game/__pycache__ src/game/*.pyc
	@rm -rf src/maze/__pycache__ src/maze/*.pyc
	@rm -rf test/__pycache__ test/*.pyc

game:
	@cd src && python3 main.py

test:
	@cd test && python3 -m unittest discover

######################################

.PHONY: setup clean  game test

#AUTHORS : ELKHAYARI Zakaria et GAUDIERE Yoni
