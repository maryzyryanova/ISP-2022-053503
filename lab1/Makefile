build:
	docker build -t lab_1 .
linter:
	python3 -m pylint lab_1.py 
run:
	docker run --rm -it --name lab_1 -v "/Users/mariazyryanova/Desktop/BSUIR/2 course/4 sem/ИСП/ISP-2022-053503/data":/lab_1/data lab_1:latest
stop: 
	docker stop lab_1