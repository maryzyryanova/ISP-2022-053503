run:
	docker run --rm -v data_volume:/data -ti --name lab_1 lab_1:volumes
stop:
	docker stop lab_1