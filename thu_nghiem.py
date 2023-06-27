# # -*- coding: utf-8 -*-
# from src.calculate_bm25_score import Inference
# from src.connect_mongodb import connect
# from src.preprocess import  clean_text, remove_number, convert_unicode
from sklearn.metrics.pairwise import cosine_similarity
# from langdetect import detect
from src.get_embedding import Embedding


# class Cal_BM25:
#     def __init__(self):
#         self.result = Inference()
#         self.embedding = Embedding()

#     '''Hàm tính toán'''
#     def BM25(self, query):
#         '''tiền xử lý văn bản'''
#         query = clean_text(query)
#         query = remove_number(query)
#         query = convert_unicode(query)
#         if query.isspace() == True or query == "":
#             return []
#         else:
#             '''Phát hiện ngôn ngữ'''
#             lan = detect(query)
#             '''Kết quả BM25'''
#             result_final_bm25 = self.result.calculate_bm25(query, lan)
#             if result_final_bm25 == []:
#                 return []
#             else:
#                 collection = connect()

#                 '''Tính điểm BM25 trung bình của các văn bản query được'''
#                 scores = [float(i[1]) for i in result_final_bm25]
#                 final_score = sum(scores) / len(scores)

#                 '''Nếu điểm của văn bản cao hơn điểm BM25 trung bình cao hơn thì sẽ append vào final_candidate'''
#                 final_candidate = [j[0] for j in result_final_bm25 if j[1] >= final_score]

#                 '''tìm cả các class đã truy vấn được'''
#                 class_ = list(set([collection.find_one({"van_ban_mau": i})["class_name"] for i in final_candidate]))
#                 '''Phân lớp'''
#                 class_or_not = []
#                 embedd_query = self.embedding.get_embeddings([query])[0]

#                 for i in class_:
#                     t = 0
#                     corsur_class = collection.find_one({"class_name": i})
#                     van_ban_mau = corsur_class['van_ban_mau']
#                     embeddings = self.embedding.get_embeddings(van_ban_mau)
#                     similarity_scores = cosine_similarity([embedd_query], embeddings)[0]

#                     if len(van_ban_mau) <= 2:
#                         if any(score >= 0.6 for score in similarity_scores):
#                             class_or_not.append(i)
#                     else:
#                         threshold = 0.6
#                         t = sum(score >= 0.6 for score in similarity_scores)
#                         if t / len(van_ban_mau) >= threshold:
#                             class_or_not.append(i)

#                 final_result = list(set(class_or_not))
#                 return final_result

embedd = Embedding()

txt1 = """Trung Quốc điều máy bay, tàu chiến áp sát Đài Loan
Trung Quốc triển khai loạt máy bay quân sự và tàu chiến hoạt động quanh đảo Đài Loan, sau khi thông báo mở đợt diễn tập lớn ở khu vực."""

txt2 = "Mỹ-Philippines tập trận lớn nhất 30 năm ở Biển Đông, eo biển Đài Loan (PLO)- Mỹ và Philippines đã khởi động cuộc tập trận chiến đấu lớn nhất trong nhiều thập niên trên vùng Biển Đông và eo biển Đài Loan. Đây là lần đầu tiên lực lượng đồng minh sử dụng đạn thật trong tập trận ở Biển Đông."
txt3 = "Mỹ - Philippines lên án các hành động khiêu khích của Trung Quốc ở Biển Đông Lần đầu tiên kể từ 7 năm qua, Mỹ và Philippines nhóm họp bộ trưởng Ngoại Giao và Quốc Phòng tại Washington ngày 11/04/2023. Thông cáo chung sau cuộc họp khẳng định « lập trường chung » về các vấn đề khu vực và quốc tế, đồng thời « phản đối mạnh mẽ » hành động bành trướng, khiêu khích của Trung Quốc ở Biển Đông. "
txt4 = "Philippines tung đối sách mạnh ứng phó Trung Quốc ở Biển Đông Không chỉ đổi mới biện pháp phản ứng, tuần duyên Philippines còn hướng đến việc vô hiệu hóa chiến lược vùng xám mà Trung Quốc thực thi ở Biển Đông."

print(cosine_similarity(embedd.get_embeddings([txt1]), embedd.get_embeddings([txt2])))
print(cosine_similarity(embedd.get_embeddings([txt1]), embedd.get_embeddings([txt3])))
print(cosine_similarity(embedd.get_embeddings([txt1]), embedd.get_embeddings([txt4])))