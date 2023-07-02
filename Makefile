dev:
	docker-compose up {{tempalte_name}}_api

rename:
    @read -p "Enter name for this application:" name; \
    name_replace $$name
