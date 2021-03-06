FILE=toc.py
RUNNER=python3

TEST_MD_FILE=test.md

fmt:
	isort $(FILE)
	black $(FILE)

testdoc:
	@$(RUNNER) $(FILE) $(TEST_MD_FILE)

clean:
	$(RM) -r __pycache__ .pytest_cache

.PHONY: clean

