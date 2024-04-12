dev:
	docker-compose up {{template_name}}_api

rename:
	@echo "Enter a project name: "; \
	read proj_name; \
	bash ./name_replacer.sh "$$proj_name"
