def palindrom(str, start,end):
    if start >= end:
        return True
        
    if str[start] != str[end]:
        return False

    return palindrom(str, start+1, end-1)

def is_palindrom(str):
    return palindrom(str, 0, len(str)-1)

if __name__ == '__main__':
    a = 'malayalam'
    print(is_palindrom(a))