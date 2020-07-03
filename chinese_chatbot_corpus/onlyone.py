import os
from config import Config
from process_pipelines.ptt import remove_duplicate_symbols

def process_all_corpus():
    remove_duplicate_symbols()
  
if __name__ == '__main__':
    process_all_corpus()