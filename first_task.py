import string
# import requests

alphabet = {letter: int(index) for index, letter in enumerate(string.ascii_uppercase, start=1)}
name_position = 0


def alphabet_position(name, cnt=0):
    global name_position
    name_position += 1
    cnt += sum(alphabet[letter] for letter in name)
    return cnt * name_position


# Работа со скачанным файлом
with open('names.txt') as f:
    print(*[sum(alphabet_position(name[1:-1]) for name in sorted(f.read().split(',')))])

# # Решение без скачивания файла с помощью get-запроса
# response = requests.get("https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c47a2634-d6cf-4b2b-9229-95fbdbe92cae/names.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200812T130911Z&X-Amz-Expires=86400&X-Amz-Signature=89e04956764357f9d0a0fd69f2436674ab74d4a6d4993119e39f30667fa66a02&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22names.txt%22").text
# print(*[sum(alphabet_position(name[1:-1]) for name in sorted(response.split(',')))])

# answer = 871853874
