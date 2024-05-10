init:
	code --install-extension ms-python.debugpy
	code --install-extension ms-python.python
	code --install-extension ms-python.vscode-pylance
	cp .env.example .env
	pip install -r requirements.txt