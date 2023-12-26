file_path = "/home/ec2-user/environment/10/bbs_notes.txt"

def new_comment():
    
    f = open(file_path, "r", encoding="UTF-8")
    
    #define "lines"
    lines = f.readlines()
    
    #close file
    f.close
    
    #print previous comments
    print("投稿一覧 -------")
    
    #print lines in reversed order
    for line in reversed(lines):
        print(line.rstrip())
        
    #ask for name
    print("名前を入力して下さい。")
    text_NAME = input()
    
    #ask for comment
    print("コメントを入力して下さい。")
    text_COMM = input()
    
    #open text file with addendum
    f = open(file_path, "a", encoding="UTF-8")
    
    #write to file
    f.write("\n" + text_NAME + "：" + text_COMM)
    
    #close file
    f.close()
    
    #open text file with read
    f = open(file_path, "r", encoding="UTF-8")
    
    #define "lines"
    lines = f.readlines()
    
    #close file
    f.close
    
    #print previous comments
    print("投稿一覧 -------")
    
    #print lines in reversed order
    for line in reversed(lines):
        print(line.rstrip())

new_comment()

#ask to continue FUNC
def cont_ques():
    #print and wait for input
    print("0:終了する 1:書き込む")
    cont_ans = input()
    
    #if 0 "end"
    if cont_ans in ["0"]:
        print("終了します")
    
    #if 1 write again    
    elif cont_ans in ["1"]:
        new_comment()
        cont_ques()
    
    #display error and repeat ask
    else:
        print("エラー：0か１で入力してください")
        cont_ques()

cont_ques()
