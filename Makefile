.PHONY: configure
configure:
	pip install -r requirements.txt

.PHONY: simulate
simulate:
	python ./run.py

.PHONY: model
model:
	python ./model/model.py

.PHONY: analyse
analyse:
	Rscript ./analyse/analyse.r
