def solution(snippet, message):    
    # 문자열은 공백으로 구분하는 단어 단위로 대치 가능 (문제 마지막 줄 참조)
    splitted_messages = message.split(' ')
    
    for [shorten, origin] in snippet:
        # 분절된 단어 단위 반복
        for idx, message_fragment in enumerate(splitted_messages):
            # NOTE: replace 함수로 포함된 문자열을 바꾸는 대신, 일치하는 경우만 대체하도록 로직 변겨 
            if message_fragment == shorten:
                splitted_messages[idx] = origin
                        
    return " ".join(splitted_messages)

if __name__ == '__main__':
    solution([["msg", "message"], ["m", "me"], ["s", "see"], ["g", "group"]], "msg")