##문자열 정렬하면 ["123","123456","1324"]와 같이 정렬됨을 이용
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

#####해시를 이용하여 조회를 O(1)로 가능 코드#####
# def solution(phone_book):
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1    #hash_map에 (key,value) 저장 - key가 phone_number
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 return False
#     return True