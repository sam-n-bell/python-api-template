SHELL := /bin/bash

dev:
	docker-compose up {{template_name}}_api

rename:
	@echo "Enter a project name: "; \
	read proj_name; \
	echo "Enter 1 if using a Mac. 0 if using Windows: "; \
	read mac_yes_no; \
	bash ./name_replacer.sh "$$proj_name" "$$mac_yes_no"


