```sh

# INSTALLATION

# Ensure you're in the project root directory and your virtual environment is activated
pip install -e .

# Install the dependencies listed in requirements.txt
pip install -r requirements.txt

# Install the language model
python -m spacy download en_core_web_sm

# USAGE

# After installation, you can use 'canopy' instead of 'python3 -m canopy'

# Get a random sentence
canopy random

# Search for sentences containing a specific word
canopy word '<word>'

# Add sentences (interactive prompt)
canopy bulk

# EXAMPLES

canopy random
canopy word 'example'
canopy bulk

# Note: Replace '<word>' with actual values when using the commands

```
