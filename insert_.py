def insert():    
    import pandas as pd  
    df = pd.read_excel('data2.xlsx') 
    data = ['mike','yy',12,'男生','鎮錄完',800,'肚子'] #你新增的列
    columns = ['名字','危險因子','年紀','性別','藥物','劑量','部位']
    data = []
    for i in columns:
        a= input("請輸入"+i+":")
        data.append(a)
    df2 = pd.DataFrame([data],columns= columns)
    df= pd.concat([df2,df],ignore_index=True)
    df.to_excel('data2.xlsx', index=False)

if __name__ == "__main__":
    insert()