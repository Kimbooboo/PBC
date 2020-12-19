import tkinter as tk
import tkinter.font as tkFont
import math
from tkinter import ttk

class Nutrition(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        # self.geometry("300*150")
    

    
        # return self.record_gender

    def createWidgets(self):
        f1 = tkFont.Font(size=14, family = "Courier New")
        self.var = tk.StringVar()

        # 問年齡
        self.ageAsk = tk.Label(self, text= "請問您的年齡？", height = 1, width = 20, font=f1)
        self.ageAsk.grid(row=0, column=0)
        # 輸入年齡
        self.ageReply = tk.Entry(self, width = 8)
        self.ageReply.grid(row=0, column=1)
        # 還沒加上單位：歲
        
        # 問性別
        self.genderAsk = tk.Label(self, text= "請問您的性別？",height = 1, width = 20, font = f1)
        self.genderAsk.grid(row=1, column=0)

        self.genderM = tk.Radiobutton(self, text="男", variable=self.var, value="男")
        self.genderM.grid(row=1, column=1)
        self.genderF = tk.Radiobutton(self, text="女", variable=self.var, value="女")
        self.genderF.grid(row=1, column=2)

        # 問身高

        self.heightAsk = tk.Label(self, text= "請問您的身高？", height = 1, width = 20, font=f1)
        self.heightAsk.grid(row=2, column=0)
        self.heightReply = tk.Entry(self, width = 8)
        self.heightReply.grid(row=2, column=1)
        # 問體重
        self.weightAsk = tk.Label(self, text= "請問您的體重？", height = 1, width = 20, font=f1)
        self.weightAsk.grid(row=3, column=0)
        self.weightReply = tk.Entry(self, width = 8)
        self.weightReply.grid(row=3, column=1)
        # 問活動量
        self.activityAsk = tk.Label(self, text= "請問您的活動量為以下何種型態？", height=1, font=f1)
        self.activityAsk.grid(row=4, column=0)
        self.activityReply = ttk.Combobox(self, values=["輕度活動量", "稍輕活動量", "中度活動量", "高度活動量"])
        self.activityReply.grid(row=4, column=1)

        # 顯示活動量
        self.activityShow = tk.Label(self, text = "活動量定義參考：")
        self.activityShow1 = tk.Label(self, text = "輕度活動量：整日坐臥、沒有運動")
        self.activityShow2 = tk.Label(self, text = "稍輕活動量：整日多坐著、通勤有緩步")
        self.activityShow3 = tk.Label(self, text = "中度活動量：整日多站立、多走動")
        self.activityShow4 = tk.Label(self, text = "高度活動量：從事如運動員、搬運員等多勞動工作")

        self.activityShow.grid(row=5, column=0)
        self.activityShow1.grid(row=6, column=0)
        self.activityShow2.grid(row=7, column=0)
        self.activityShow3.grid(row=8, column=0)
        self.activityShow4.grid(row=9, column=0)
        self.calculator = tk.Button(self, text="計算您一天應攝取的熱量", command = self.click2calculateCalories)
        self.calculator.grid(row=10, column=1)
        self.showFinal = tk.Label(self, text="")
        self.showFinal.grid(row=11, column=1)

    def click2calculateCalories(self):
        height = float(self.heightReply.get())
        weight = float(self.weightReply.get())
        age = int(self.ageReply.get())
        activity = self.activityReply.get()
        gender = self.record_gender

            # 計算基礎代謝率
        if gender == "男":
            REE = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            REE = 10 * weight + 6.25 * height - 5 * age - 161

        # 加上活動量，計算總共可攝取的熱量
        if activity == "輕度活動量":
            cal = int(REE * 1.2)
        elif activity == "稍輕活動量":
            cal = int(REE * 1.375)
        elif activity == "中度活動量":
            cal = int(REE * 1.5)
        elif activity =="高度活動量":
            cal = int(REE * 1.75)

        result = "你一天應攝取的熱量為: {} 大卡".format(cal)
        self.showFinal.configure(text= result)

    def record_gender(self):
        self.record_gender = self.var.get()


            


# 重寫radio button 












        






'''
    def createWidgets(self):
        var = tk.StringVar()
        self.label = tk.Label(self, text="請問您的性別？", bg="yellow", width =15)
        self.label.pack()

        def print_selection():
            self.label.config(text="請問您的性別？"+ var.get())
        
        self.gender = tk.Radiobutton(self, text = "男", variable=var, value="男", command = print_selection)
        self.gender.pack()
        self.gender1 = tk.Radiobutton(self, text = "女", variable = var, value="女", command=print_selection)
        self.gender1.pack()
    

'''
nutri = Nutrition()
nutri.master.title("My Nutrition Calculator")
nutri.mainloop()