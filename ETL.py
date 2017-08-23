from datetime import datetime

with open('scripting_challenge_input_file.txt') as f:
    content = f.readlines()
content = [x.strip('\n').split('\t') for x in content]
headlen = len(content[0])
print(headlen)

myfile = open('output.txt', 'w')
myfile.write('Order_id\tOrder_date\tUser_id\tAvg_Item_price\tStart_page_url\Error_msg\n')
for w in content[1:]:
    error_ms = []
    if len(w) > headlen:
        w.pop()
    if w[1] == '':
        error_ms.append('User is Empty')
    if len(w[-1]) < 23 or (len(w[-1])>=23 and w[-1][:23] != 'http://www.insacart.com'):
        error_ms.append('Invalid URL')
        w[-1] = ''
    newiddate = w[0].replace('::',':').split(':')
    if len(newiddate)!=2:
        if len(newiddate)<2:
            error_ms.append('Order ID and Date Missing')
            order_id,order_date = '',''
        else:
            error_ms.append('Order ID and Date format Error')
    if len(newiddate)==2:
        order_id, order_date = newiddate[0],datetime.strptime(newiddate[1],'%Y%m%d').strftime('%Y-%m-%d')
    temp = [float(t) for t in w[2:6] if t!='' and t!= '0']
    if len(temp)!=0:
        ave = sum(temp)/len(temp)
    else:
        ave = 0
    result = [order_id,order_date,w[1],str(round(ave,2)),w[-1],','.join(error_ms)]
    myfile.write('\t'.join(result)+'\n')
myfile.close()

