class BankAccount:

    #コンストラクタ
    def __init__(self,name):#インスタンス生成時に名前引数必要
        self.name = name #名前
        self.balance = 0 #貯金
        self.interest_rate = 0.01 #金利
    
    #貯金名前出力
    def get_name(self):
        return self.name
    #貯金出力
    def get_balance(self):
        return self.balance
    #貯金追加
    def deposit(self,amount):
        self.balance += amount
    #貯金引き出し    
    def withdraw(self,amount):
        self.balance -= amount
    #金利設定
    def set_interest_rate(self,rate):
        self.interest_rate = rate

    def apply_interest(self):
        self.balance += int(self.balance*self.interest_rate)#int型にしては数切り捨て




