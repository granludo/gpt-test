# gpt-translator

By Marc Alier @granludo https://wasabi.essi.upc.edu/ludo 

Licensed under the GNU General Public License v3.0

Simple python 3 program that uses OpenAi's GPT-3.5-turbo model to translate files from one language to another. Breaks down the file into chunks of 20 lines.

## requirements

You need to have a key to use the OpenAI API  you can get one here: https://beta.openai.com/docs/developer-quickstart/api-key  this program looks for the key in a file stated in the "mykeypath" variable by default on the path '..//..//mykey.json' 

You need to install the json, and openai packages

> pip install openai
> pip install json

## usage 

> python3 gpt-translate.py origin_file origin_languaga destination_language destination_file

**Example**

> python3 gpt-translate.py sample.md catalan italian sample_translated.md 

Have fun.