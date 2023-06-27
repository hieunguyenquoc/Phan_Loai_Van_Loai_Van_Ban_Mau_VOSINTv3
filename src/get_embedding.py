from sentence_transformers import SentenceTransformer
from pyvi.ViTokenizer import tokenize


class Embedding:
    '''Khởi tạo mô hình PhoBERT'''
    def __init__(self):
        self.model = SentenceTransformer('VoVanPhuc/sup-SimCSE-VietNamese-phobert-base')
    
    '''Tiến hành embedding'''
    def get_embeddings(self, sentences):
        #st = time.time()
        #print("-------Getting embedding for document-------")
        #tokenized các câu
        sentences_tokenizer = [tokenize(sentence) for sentence in sentences]

        #tiến hành embedding (device sẽ được tự động setup)
        embeddings = self.model.encode(sentences_tokenizer)
        # print("Embedding time: ", time.time() - st)
        # print("Embedding shape :",embeddings.shape)
        return embeddings