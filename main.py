# -*- coding: utf-8 -*-
import sys
sys.path.append('D:/Aiacademy/VOSINT3_document_clustering/thu_nghiem_bm25_with_PhoBERT/src')

import time
from inference import Cal_BM25

result = Cal_BM25()

if __name__ == "__main__":
    start = time.time()
    text = "Biển Đông: Trung Quốc xuống nước sau yêu cầu của Mỹ? Kinhtedothi - Tổng thống Philippines Ferdinand Marcos Jr hôm nay (1/5) cho biết Trung Quốc đã đồng ý thảo luận về quyền đánh cá ở Biển Đông, 1 ngày sau khi Mỹ yêu cầu Bắc Kinh ngừng quấy rối các tàu Philippines tại vùng biển này."
    # start0 = time.time()
    # print("Time to load :", time.time() - start0)
    print(result.BM25(text))
    print("Time :", time.time()-start)