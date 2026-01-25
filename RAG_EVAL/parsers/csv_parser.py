import csv
import json

import sys
import os

# Добавляем родительскую директорию (NIR) в пути поиска Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from normalization.schema import RAGRecord

#Вход csv : query,answer,retrieved_docs,prompt
class Parser:
    rag_records = list[RAGRecord]

    def __init__(self):
        self.rag_records = []

    def parse(self, file_path):
        with open (file_path, encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader,None)
            for line_num, row in enumerate(reader, start=1):
                try:
                    rag_record = RAGRecord(
                        query = row[0],
                        answer = row[1],
                        retrieved_docs = json.loads(row[2]), #if row[2] else [],
                        prompt = row[3]
                    )                
                    self.rag_records.append(rag_record)
                    print(f"Строка {line_num}  успешно загружена")
                except Exception as e:
                    print(f"При обработке {line_num} строки возникла ошибка")
            print(f"Успешно обработано {len(self.rag_records)} строк")
        return self.rag_records

parser = Parser()
(parser.parse("rag_logs.csv"))

