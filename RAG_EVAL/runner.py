from parsers.csv_parser import Parser
from utils.sentence_splitter import TextSplitter
from embeddings.embedder import Embedder

parser = Parser()
rag_records = parser.parse(r"D:\RAG_evaluation\RAG_EVAL\rag_logs.csv")

RAGRecord = rag_records[0]

answer = RAGRecord.answer
retrieved_docs = RAGRecord.retrieved_docs
docs = [Doc.text for Doc in retrieved_docs]

splitter = TextSplitter()
split_answer = splitter.split_text(answer)
split_docs = [splitter.split_text(doc) for doc in docs]

print(split_answer, '\n',split_docs )

emdebber = Embedder('paraphrase-multilingual-MiniLM-L12-v2')
answer_embedding = emdebber.encode(split_answer)
print(answer_embedding.items())






