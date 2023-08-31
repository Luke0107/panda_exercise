def update():
    import pandas as pd
    df = pd.read_excel('data2.xlsx')
    name = input('請輸入名字:')
    ele = ['危險因子','年紀','性別','藥物','劑量','部位']
    for i in ele:
        answer = input('請輸入'+i+'，不輸即不修改:')
        if answer!="":
            df.loc[df['名字'] ==name, i] = answer
    df.to_excel('data2.xlsx',index=False)
if __name__=="__main__":
    update()