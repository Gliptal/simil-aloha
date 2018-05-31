.PHONY: configure
configure:
	pip install colorclass                 && \
	pip install numpy                      && \
	pip install terminaltables             && \

.PHONY: simulate
simulate:
	python ./run.py

.PHONY: model
model:
	python ./model/model.py

.PHONY: analyse
analyse:
	Rscript ./analyse/analyse.r
