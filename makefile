# To install all of the dependencies locally
install:
	pip3 install -r requirements.txt

# Main command to run the app locally
run:
	python3 index.py

# Save everything that is installed into the requirements.txt
save:
	pip3 freeze > requirements.txt
