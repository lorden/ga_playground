"""Script to clean Github release notes syntax for a Slack message."""
import os
import re
import sys

def clean_notes(notes):
  # Remove comments
  clean_notes = re.sub("(<!--.*?-->)", "", notes, flags=re.DOTALL)

  # Transform new lines
  clean_notes = re.sub(r'\\r\\n', '\n', clean_notes)

  # Change bullet points
  clean_notes = re.sub(r'\* (.*)', r'• \1', clean_notes)

  # Change h3 titles
  # clean_notes = re.sub(r'### (.*)', r'*_\1_*', clean_notes)
  clean_notes = re.sub(r'### (.*)', r'*\1*', clean_notes)

  # Change h2 titles
  clean_notes = re.sub(r'## (.*)', r'*\1*', clean_notes)

  return clean_notes.strip()

def set_env_var(name, content):
  env_file = os.getenv('GITHUB_ENV')
  with open(env_file, 'a') as ef:
    ef.write(f'{name}={content}')

if __name__ == '__main__':
  notes = clean_notes(sys.argv[1])
  set_env_var('RELEASE_NOTES', notes)
