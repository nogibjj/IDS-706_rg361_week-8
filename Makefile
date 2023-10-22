install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv  --cov=main --cov=codes codes/test_main.py
# cargo test --quiet --manifest-path ./codes/Cargo.toml

format:	
	black codes/*.py
	cargo fmt --manifest-path ./codes/Cargo.toml

lint:
	ruff check codes/*.py
	cargo clippy --quiet --manifest-path ./codes/Cargo.toml

deploy:
	#deploy goes here
		
all: install test format lint deploy