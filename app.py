import os
import openai
import ast
from pprint import pprint
import re
import argparse

openai.api_key_path = '.env'

def read_text(path):
    # path is a file
    if os.path.isfile(path):
        with open(file) as f:
            return f.readlines()
    # path is a directory
    files_text = []
    files = os.listdir(path)
    for file in files:
        with open(path+'/'+file) as f:
            contents = f.readlines()
            files_text.append(contents)
    return files_text
    
parser = argparse.ArgumentParser()
parser.add_argument("-path", help="path to generated files (can be a directory or file)")
args = parser.parse_args()

if not os.path.exists(args.path):
    print("Error: {} doesn't exist.".format(args.path))

text = read_text(args.path)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Given this file: {}, Generate an example grpcurl command for each endpoint with example data.".format(text),
  temperature=0.5,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.2,
  presence_penalty=0.0,
  stop=["\n"]
)

print(response)