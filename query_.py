def query():
    import pandas as pd  
    df = pd.read_excel('data2.xlsx')
    
    name = input('請輸入名字:')
    name = name.capitalize()
    while True:
        try:
            print(df[df['名字']==name])
            break
        except:
            print('None Exist')

if __name__ == "__main__":
    query()