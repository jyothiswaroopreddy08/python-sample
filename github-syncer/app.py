import yaml

# Read the config.yaml file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Extract the parameters
build_type = config['buildType']
deploy_type = config['deployType']
env_mapping = config['envMapping']

# Generate the GitHub Actions workflow YAML
workflow_yaml = f"""
name: Build and Deploy

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x
      
      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Build
        run: |
          # Build script based on buildType parameter: {build_type}
      
      - name: Deploy
        run: |
          # Deploy script based on deployType parameter: {deploy_type}
      
      - name: Set environment mapping
        run: |
          # Set environment mapping based on envMapping parameter: {env_mapping}
"""

# Save the generated YAML to a file
with open('.github/workflows/workflow.yaml', 'w') as file:
    file.write(workflow_yaml)
