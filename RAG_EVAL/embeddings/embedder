from sentence_transformers import SentenceTransformer

class Embedder:
     
    def __init__(self, model_name):
        model = SentenceTransformer(model_name)
        self.model = model

    def encode(self,texts):

        embeddings = self.model.encode(texts)
        encoded_data = dict(zip(texts, embeddings))
        
        return encoded_data
    

