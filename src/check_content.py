def check_content_ev(title, content):
    content_ev = title + ". " + content
    lst_content_ev = content_ev.split(".")[:5]
    result = ".".join(lst_content_ev)
    return result

print(check_content_ev("Khó tiếp cận nhà xã hội giá rẻ vì thiếu phân khúc cho thuê","Chủ nhiệm Ủy ban Kinh tế cho rằng không chỉ giá nhà quá cao, việc thiếu hụt phân khúc cho thuê cũng khiến lao động khó tiếp cận nhà ở xã hội giá rẻ. "))