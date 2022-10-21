"""Script to clean Github release notes syntax for a Slack message."""
import os
import re
import sys

def clean_notes(notes):
  # Remove comments
  clean_notes = re.sub("(<!--.*?-->)", "", notes, flags=re.DOTALL)

  # Change h2 titles
  clean_notes = re.sub('##(.*)\r\n', r'*\1*', clean_notes)

  # Change h3 titles
  clean_notes = re.sub('###(.*)\r\n', r'*_\1_*', clean_notes)

  # Change bullet points
  clean_notes = re.sub('\n\* (.*)\r\n', r'• \1', clean_notes)

  env_file = os.getenv('GITHUB_ENV')
  with open(env_file, 'a') as ef:
    ef.write(f'RELEASE_NOTES={clean_notes}')

if __name__ == '__main__':
  clean_notes(sys.argv[1])
