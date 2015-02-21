PREFIX=/usr/local

install:
	cp -f bin/vagabond $(PREFIX)/bin/vagabond

uninstall:
	rm -f $(PREFIX)/bin/vagabond

.PHONY: install uninstall
