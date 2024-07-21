import os
import re

pattern = re.compile(r'^(?!.*\.preview).*\.py$')  # Replace with your regex pattern
files_to_execute = [f for f in os.listdir('../') if pattern.match(f) and f.endswith('.py')]
