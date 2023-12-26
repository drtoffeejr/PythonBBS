file_path = "/bbs.txt"

def new_comment():
    
    f = open(file_path, "r", encoding="UTF-8")
    
    lines = f.readlines()
    
    f.close
    
    print("投稿一覧 -------")
    
    for line in reversed(lines):
        print(line.rstrip())
        
    print("名前を入力して下さい。")
    text_NAME = input()
    
    print("コメントを入力して下さい。")
    text_COMM = input()
    
    f = open(file_path, "a", encoding="UTF-8")
    
    f.write("\n" + text_NAME + "：" + text_COMM)
    
    f.close()
    
    f = open(file_path, "r", encoding="UTF-8")
    
    lines = f.readlines()
    
    f.close
    
    print("投稿一覧 -------")
    
    for line in reversed(lines):
        print(line.rstrip())

new_comment()

def cont_ques():
    
    print("0:終了する 1:書き込む")
    cont_ans = input()
    
    if cont_ans in ["0"]:
        print("終了します")
       
    elif cont_ans in ["1"]:
        new_comment()
        cont_ques()
    
    else:
        print("エラー：0か１で入力してください")
        cont_ques()

cont_ques()
