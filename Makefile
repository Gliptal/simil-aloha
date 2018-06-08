.PHONY: configure
configure:
	pip3 install -r requirements.txt

.PHONY: simulate
simulate:
	python3 ./run.py

.PHONY: model
model:
	python3 ./model/model.py

.PHONY: analyse
analyse:
	Rscript ./analyse/analyse.r
