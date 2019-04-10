APP_NAME = idb
PROJ_PHASE = 3

IDB_LOG := IDB$(PROJ_PHASE).log

FILES := \
	.gitignore \
	$(IDB_LOG)

# Set Windows/Unix specific commands.
ifeq ($(shell uname -p), unknown)
	# Windows
	LAUNCH := FLASK_APP=$(APP_NAME); flask run --port 8000
	WHICH := where
else
	# Linux/macOS
	LAUNCH := gunicorn -w 4 $(APP_NAME):app
	WHICH := which
endif

# Stop if conda isn't installed.
ifeq (,$(shell $(WHICH) conda))
	$(error "Please make sure conda is installed.")
endif

check:
	@not_found=0; \
	for i in $(FILES); do \
	  if [ -e $$i ]; then \
            echo "$$i found"; \
          else \
            echo "$$i NOT FOUND"; \
            not_found=`expr "$$not_found" + "1"`; \
          fi \
        done; \
	if [ $$not_found -ne 0 ]; then \
          echo "$$not_found failures"; \
          exit 1; \
	fi; \
	echo "success";

config:
	git config -l

deploy-local:
	$LAUNCH

update-environment:
	conda update -n base conda
	conda env update -f environment.yml

.PHONY: $(IDB_LOG)
$(IDB_LOG):
	git log > $(IDB_LOG)

.PHONY: clean
clean:
	rm -rf idb/templates/gen
	rm -rf idb/static/gen
	rm -f $(IDB_LOG)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

status:
	make clean
	@echo
	git --no-pager branch
	git remote -v
	git status

