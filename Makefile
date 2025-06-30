JEP_JAR = libs/jep-4.2.2.jar
JEP_SO_DIR = venv/lib/*/site-packages/jep

all: venv install clean src/main/java/Main.class js

venv:
	virtualenv venv

install:
	venv/bin/pip install -r requirements.txt

clean:
	rm -f src/main/java/Main.class

src/main/java/Main.class: src/main/java/Main.java
	javac -cp ${JEP_JAR} src/main/java/Main.java

js:
	esbuild src/main/javascript/main.js --bundle --outfile=app/static/js/global/jungle.bundle.js --minify

run: all
	java -cp src/main/java:${JEP_JAR} -Djep.library.path=${JEP_SO_DIR} Main

test:
	bash tests/tests.sh
