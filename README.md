# Python Build and Packaging
## Install
### Create and activate a venv named .venv
`/path/to/python3 -m venv .venv`

`source .venv/bin/activate`

### Install your Python app
#### Add -e if you require editable
`pip install -e .` (see requirements.txt)

## Run the installed program
`run-advice` (see pyproject.toml)

## Package the program
This generates a dist directory containing a .tar.gz and a .whl

`python -m build`

The .whl is a self-contained Python program installable in another venv!

`mkdir -p /tmp/should_i_use_a_venv_2`

`cp should_i_use_a_venv*.whl /tmp/should_i_use_a_venv_2`

`cd /tmp/should_i_use_a_venv_2`

`/path/to/python3 -m venv .venv`

`pip install should_i_use_a_venv*.whl`

`run-advice`
