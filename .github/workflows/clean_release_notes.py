"""Script to clean Github release notes syntax for a Slack message."""
import os
import re
import sys

def clean_notes(notes):
  # Remove comments
  clean_notes = re.sub("(<!--.*?-->)", "", notes, flags=re.DOTALL)

  # Change h2 titles
  clean_notes = re.sub('\n## (.*?)\n', r'\n*\1*\n', clean_notes)

  # Change h3 titles
  clean_notes = re.sub('\n### (.*?)\n', r'\n*_\1_*\n', clean_notes)

  # Change bullet points
  clean_notes = re.sub('\n\* (.*?)\n', r'\n• \1\n', clean_notes, flags=re.DOTALL)

  return clean_notes

def set_env_var(name, content):
  env_file = os.getenv('GITHUB_ENV')
  with open(env_file, 'a') as ef:
    ef.write(f'{name}={content}')

if __name__ == '__main__':
  notes = clean_notes(sys.argv[1])
  set_env_var('RELEASE_NOTES', notes)
