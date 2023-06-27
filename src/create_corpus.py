from underthesea import word_tokenize
from connect_mongodb import connect

class Create_corpus_vi:
    def __init__(self):
        self.cursor = connect().find({})
        
    '''Hàm tạo tập dữ liệu tiếng Việt'''
    def Create_corpus_vi(self):
        self.corpus_tst_vi = []
        '''Kết nối tới cơ sở dữ liệu mongo'''
        
        for i in self.cursor:
            if i["van_ban_mau"] is None or i["van_ban_mau"] == "":
                continue
            else:
                self.corpus_tst_vi.extend(i["van_ban_mau"])


    '''Hàm tạo dữ liệu được tokenize tiếng Việt'''
    def Create_tokenized_corpus_vi(self):
        #Tập tất cả các từ trong mongodb
        self.tokenized_corpus_vi = [word_tokenize(doc) for doc in self.corpus_tst_vi]


# result = Create_corpus()
# print(result.Create_corpus_en())