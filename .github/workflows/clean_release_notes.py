"""Script to clean Github release notes syntax for a Slack message."""
import os
import re

def clean_notes(notes):
  clean_notes = re.sub("(<!--.*?-->)", "", notes, flags=re.DOTALL)

  env_file = os.getenv('GITHUB_ENV')
  with open(env_file) as ef:
    ef.write(f'RELEASE_NOTES={clean_notes}')

if __name__ == '__main__':
  clean_notes(argv[1])
