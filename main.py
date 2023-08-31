from insert_ import insert
from query_ import query
from delete_ import delete
from update_ import update
while True:
    choice =input("(1)新增(2)查詢(3)刪除(4)更改(5)結束程式：")
    if choice =='1':
        insert()
    elif choice=='2':
        query()
    elif choice=='3':
        delete()
    elif choice=='4':
        update()
    elif choice=='5':
        print("結束程式！")
        break
    else:
        print("無效指令！")