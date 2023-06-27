# -*- coding: utf-8 -*-
from calculate_bm25_score import Inference
from connect_mongodb import connect
from preprocess import  clean_text, remove_number, convert_unicode
from sklearn.metrics.pairwise import cosine_similarity
from get_embedding import Embedding


class Cal_BM25:
    def __init__(self) :
        self.result = Inference()
        self.embedding = Embedding()

    '''Hàm tính toán'''
    def BM25(self,query):
        '''tiền xử lý văn bản'''
        query = clean_text(query)
        query = remove_number(query)
        query = convert_unicode(query)
        if query.isspace()==True or query == "":
            return []
        else:
            '''Phát hiện ngôn ngữ'''
            '''Kết quả BM25'''
            result_final_bm25 = self.result.calculate_bm25(query)
            if result_final_bm25 == []:
                return []
            else:
                collection = connect()

                '''Tính điểm BM25 trung bình của các văn bản query được'''
                score = sum([float(i[1]) for i in result_final_bm25])
                final_score = score/len(result_final_bm25)

                '''Nếu điểm của văn bản cao hơn điểm BM25 trung bình cao hơn thì sẽ append vào final_candidate'''
                final_candidate = [j[0] for j in result_final_bm25 if j[1] >= final_score]

                '''tìm cả các class đã truy vấn được'''
                class_ = list(set([collection.find_one({"van_ban_mau": i})["class_name"] for i in final_candidate]))
                '''Phân lớp'''
                class_or_not = []
                embedd_query = self.embedding.get_embeddings([query])[0]
                
                for i in class_:
                    t = 0
                    corsur_class = collection.find_one({"class_name": i})
                    van_ban_mau = corsur_class['van_ban_mau']
                    embeddings = self.embedding.get_embeddings(van_ban_mau)
                    similarity_scores = cosine_similarity([embedd_query], embeddings)[0]
                    threshold_for_cosine = 0.5
                    if len(van_ban_mau) <= 2:
                        if any(score >= threshold_for_cosine for score in similarity_scores):
                            class_or_not.append(i)
                    else:
                        threshold_classifier = 0.6
                        t = sum(score >= threshold_for_cosine for score in similarity_scores)
                        if t / len(van_ban_mau) >= threshold_classifier:
                            class_or_not.append(i)
                final_result = list(set(class_or_not))
                return final_result