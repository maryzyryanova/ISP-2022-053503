run:
	docker run -v "/Users/mariazyryanova/Desktop/BSUIR/2 course/4 sem/ИСП/ISP-2022-053503/data:/lab_1" -v data_volumes:/lab_1/data --rm -ti --name lab_1 lab_1:volume
stop:
	docker stop lab_1