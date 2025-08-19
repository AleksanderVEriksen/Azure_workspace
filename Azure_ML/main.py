import click
from transformers import pipeline
import urllib.request as Request
from bs4 import BeautifulSoup

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"

def get_text_from_url(url):
    text = ""
    req = Request(url,
                data=None,
                headers={'User-Agent': 'Mozilla/5.0'})
    html = Request.urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')
    for paragraph in soup.find_all('p'):
        text += paragraph.get_text() + "\n"
    return text.strip()

def process(text):
    summarizer = pipeline("summarization", model='t5-small')
    summary = summarizer(text, max_length=130)
    click.echo("Summary completed.")

    return summary[0]['summary_text']

@click.command()
@click.option('--url')
@click.option('--file')
def main(url, file):
    if url:
        text = get_text_from_url(url)
    elif file:
        with open(file, 'r') as f:
            text = f.read()
    click.echo("Summarized text from -> {}".format(url if url else file))
    click.echo(process(text))