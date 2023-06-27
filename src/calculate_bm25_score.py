# -*- coding: utf-8 -*-
from create_corpus import Create_corpus_vi
from underthesea import word_tokenize
from rank_bm25.rank_bm25 import BM25Okapi

class Inference:
    def __init__(self):
        '''
        Các tham số mặc định
        '''
        # self.corpus_tst = []
        #tính BM25 với tiếng Việt
        self.create_corpus_vi = Create_corpus_vi()
        self.create_corpus_vi.Create_corpus_vi()
        self.create_corpus_vi.Create_tokenized_corpus_vi()

        #lấy bao nhiêu văn bản liên quan
        self.top_n = 10

    '''Hàm tính toán bm25'''
    def calculate_bm25(self, query):
        #truyền vào bộ corpus tiếng Việt đã được tokenize
        if self.create_corpus_vi.tokenized_corpus_vi == []:
            return []
        else:
            bm25 = BM25Okapi(self.create_corpus_vi.tokenized_corpus_vi)
            #tokenize câu tiếng Việt
            tokenized_query = word_tokenize(query) 

            #tìm top n câu liên quan nhất
            relevant_doc = bm25.get_top_n(tokenized_query,self.create_corpus_vi.corpus_tst_vi, n=self.top_n)
            return relevant_doc
        
    