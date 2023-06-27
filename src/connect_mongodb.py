import pymongo

def connect():
    #return bảng dữ liệu trong csdl
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["document_cluster_title_content"]
    my_col = mydb["cluster"]
    return my_col