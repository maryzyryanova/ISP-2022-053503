run:
	docker run -d -p 3000:3000 -v "/Users/mariazyryanova/Desktop/BSUIR/2 course/4 sem/ИСП/ISP-2022-053503:/app" -v data_volume:/lab_1/data -ti --rm --name lab_1 lab_1:volumes
stop:
	docker stop lab_1