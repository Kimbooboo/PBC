import tkinter as tk
import tkinter.font as tkFont
import math
from tkinter import ttk


typeList = ["全穀根莖類", "蔬菜類", "水果類", "油脂與堅果種子類", "蛋豆魚肉類(高脂)", "蛋豆魚肉類(中脂)", "蛋豆魚肉類(低脂)", "奶類(全脂)", "奶類(低脂)", "奶類(脫脂)"]
unit_cal_list = [70, 25, 60, 45, 120, 75, 55, 150, 120, 80]
this_meal_consume = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total_consume = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
meal_consume = 0
calories_quota = 0
class Nutrition(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        # self.geometry("300*150")

        # return self.record_gender

    def createWidgets(self):
        f1 = tkFont.Font(size=14, family="Courier New")
        self.var = tk.StringVar()

        # 問年齡
        self.ageAsk = tk.Label(self, text="請問您的年齡？", height=1, width=20, font=f1)
        self.ageAsk.grid(row=0, column=0)
        # 輸入年齡
        self.ageReply = tk.Entry(self, width=8)
        self.ageReply.grid(row=0, column=1)
        # 還沒加上單位：歲

        # 問性別
        self.genderAsk = tk.Label(self, text="請問您的性別？", height=1, width=20, font=f1)
        self.genderAsk.grid(row=1, column=0)

        self.genderM = tk.Radiobutton(self, text="男", variable=self.var, value="男")
        self.genderM.grid(row=1, column=1)
        self.genderF = tk.Radiobutton(self, text="女", variable=self.var, value="女")
        self.genderF.grid(row=1, column=2)

        # 問身高

        self.heightAsk = tk.Label(self, text="請問您的身高？", height=1, width=20, font=f1)
        self.heightAsk.grid(row=2, column=0)
        self.heightReply = tk.Entry(self, width=8)
        self.heightReply.grid(row=2, column=1)
        # 問體重
        self.weightAsk = tk.Label(self, text="請問您的體重？", height=1, width=20, font=f1)
        self.weightAsk.grid(row=3, column=0)
        self.weightReply = tk.Entry(self, width=8)
        self.weightReply.grid(row=3, column=1)
        # 問活動量
        self.activityAsk = tk.Label(self, text="請問您的活動量為以下何種型態？", height=1, font=f1)
        self.activityAsk.grid(row=4, column=0)
        self.activityReply = ttk.Combobox(self, values=["輕度活動量", "稍輕活動量", "中度活動量", "高度活動量"])
        self.activityReply.grid(row=4, column=1)

        # 顯示活動量
        self.activityShow = tk.Label(self, text="活動量定義參考：")
        self.activityShow1 = tk.Label(self, text="輕度活動量：整日坐臥、沒有運動")
        self.activityShow2 = tk.Label(self, text="稍輕活動量：整日多坐著、通勤有緩步")
        self.activityShow3 = tk.Label(self, text="中度活動量：整日多站立、多走動")
        self.activityShow4 = tk.Label(self, text="高度活動量：從事如運動員、搬運員等多勞動工作")

        self.activityShow.grid(row=5, column=0)
        self.activityShow1.grid(row=6, column=0)
        self.activityShow2.grid(row=7, column=0)
        self.activityShow3.grid(row=8, column=0)
        self.activityShow4.grid(row=9, column=0)
        self.calculator = tk.Button(self, text="計算您一天應攝取的熱量", command=self.click2calculateCalories)
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
        global calories_quota

        if activity == "輕度活動量":
            cal = int(REE * 1.2)
            calories_quota = cal
        elif activity == "稍輕活動量":
            cal = int(REE * 1.375)
            calories_quota = cal
        elif activity == "中度活動量":
            cal = int(REE * 1.5)
            calories_quota = cal
        elif activity == "高度活動量":
            cal = int(REE * 1.75)
            calories_quota = cal



# 進入page2

        import tkinter as tk
        from tkinter import ttk

        class Page2(tk.Frame):
            def __init__(self):
                tk.Frame.__init__(self)
                self.grid()
                self.createWidgets()

            def createWidgets(self):

        # 調整字體
                import tkinter.font as tkFont
                f1 = tkFont.Font(size = 16, family = "微軟正黑體")

        #  標題
                self.Calories_quota_label = tk.Label(self, text = "本人今日熱量餘額為" + str(calories_quota) + "大卡", font = f1)
                self.Calories_quota_label.grid(row = 0, column = 0)

        # 食物類別選單
                self.type = tk.StringVar()
                self.type.set("食物類別")
                self.optionmenu = tk.OptionMenu(self, self.type, *typeList)
                self.optionmenu.grid(row = 1, column = 0, sticky = tk.N + tk.W)
                self.optionmenu.config(font = f1)

        # 單位選擇
                self.unit = tk.Spinbox(self, from_=0, to=10, increment = 0.5, font = f1)
                self.unit.grid(row = 2, column = 0, sticky = tk.N + tk.W)
                unit_label = tk.Label(self, text = "份", font = f1)
                unit_label.grid(row = 2, column = 1)

        # 下一個食物
                self.nxt_foodbtn = tk.Button(self, text = "確定", font = f1, command = self.nxt_food_cmd)
                self.nxt_foodbtn.grid(row = 4, column = 0, sticky = tk.N + tk.W)
        # 此餐統計
                self.end_inputbtn = tk.Button(self, text = "此餐統計", font = f1, command = self.this_meal_sum)
                self.end_inputbtn.grid(row = 6, column = 0, sticky = tk.N + tk.W)

        # 吃了甚麼
                self.eaten_label = tk.Label(self, text ="", font = f1)
                self.eaten_label.grid(row = 5, columnspan = 3)



        ### listener

            def nxt_food_cmd(self):
        # 運算
                food_index = typeList.index(self.type.get())
                unit_cal_consume = unit_cal_list[food_index]
                unit = float(self.unit.get())
                this_meal_consume[food_index] += unit
                calories_consume = unit_cal_consume*unit
        # 字體
                import tkinter.font as tkFont
                f1 = tkFont.Font(size = 16, family = "微軟正黑體")
        # output
                self.eaten_label.configure(text = self.eaten_label.cget("text") + "\n" + str(self.type.get()) + str(unit) + "份" + str(calories_consume) +"大卡", font = f1)
        # 歸零按鈕
                self.type.set("食物類別")
                self.unit.delete(0, "end")
                self.unit.insert(0, 0.0)
                global meal_consume
                meal_consume += calories_consume



            def this_meal_sum(self):

                global this_meal_consume
                global total_consume

        # 創表
                p3 = tk.Toplevel()
                tree = ttk.Treeview(p3)
                p3.title("此餐統計")
                tree["columns"]=("蛋白質","脂肪","醣類")
                tree.column("蛋白質",width=100)   #表示列,不顯示
                tree.column("脂肪",width=100)
                tree.column("醣類",width=100)

                tree.heading("蛋白質",text="蛋白質")  #顯示錶頭
                tree.heading("脂肪",text="脂肪")
                tree.heading("醣類",text="醣類")


                tree.insert("",0,text="全穀根莖類" + str(this_meal_consume[0]) + "份" ,values=(2*this_meal_consume[0],"-",15*this_meal_consume[0])) #插入資料，
                tree.insert("",1,text="蔬菜類" + str(this_meal_consume[1]) + "份" ,values=(1*this_meal_consume[1],"-",5*this_meal_consume[1]))
                tree.insert("",2,text="水果類" + str(this_meal_consume[2]) + "份" ,values=("-", "-", 15*this_meal_consume[2]))
                tree.insert("",3,text="油脂與堅果種子類" + str(this_meal_consume[3]) + "份" ,values=(1.5*this_meal_consume[3],5*this_meal_consume[3],"-"))
                tree.insert("",4,text="蛋豆魚肉類(高脂)" + str(this_meal_consume[4]) + "份" ,values=(7*this_meal_consume[4], 3*this_meal_consume[4], "-"))
                tree.insert("",5,text="蛋豆魚肉類(中脂)" + str(this_meal_consume[5]) + "份" ,values=(7*this_meal_consume[5], 5*this_meal_consume[5], "-"))
                tree.insert("",6,text="蛋豆魚肉類(低脂)" + str(this_meal_consume[6]) + "份" ,values=(7*this_meal_consume[6],10*this_meal_consume[6],12*this_meal_consume[6]))
                tree.insert("",7,text="奶類(全脂)" + str(this_meal_consume[7]) + "份" ,values=(8*this_meal_consume[7],8*this_meal_consume[7],12*this_meal_consume[7]))
                tree.insert("",8,text="奶類(低脂" + str(this_meal_consume[8]) + "份" ,values=(8*this_meal_consume[8],4*this_meal_consume[8],12*this_meal_consume[8]))
                tree.insert("",9,text="奶類(脫脂)" + str(this_meal_consume[9]) + "份" ,values=(8*this_meal_consume[9],"-",12*this_meal_consume[9]))

                tree.pack()

        # 運算
                global meal_consume

                global calories_quota
                self.Calories_quota_label.configure(text = "本人今日熱量餘額為" + str(calories_quota - meal_consume) + "大卡")

                calories_quota -= meal_consume
                meal_consume = 0

        # 加進今日
                for i in range(10):
                    total_consume[i] += this_meal_consume[i]
                    this_meal_consume[i] = 0


        # 清除此餐內容
                self.eaten_label.configure(text ="")


        #  今日結算按鈕
                import tkinter.font as tkFont
                f1 = tkFont.Font(size = 16, family = "微軟正黑體")
                self.today_sum_btn = tk.Button(text = "今日結算", font = f1, command = self.TDSum_Cmd)
                self.today_sum_btn.grid(row = 8, columnspan = 3)


            def TDSum_Cmd(self):

                for i in range(10):
                    total_consume[i] += this_meal_consume[i]
                    this_meal_consume[i] = 0

                p4 = tk.Toplevel()
                tree = ttk.Treeview(p4)
                p4.title("今日統計")
                tree["columns"]=("蛋白質","脂肪","醣類")
                tree.column("蛋白質",width=100)   #表示列,不顯示
                tree.column("脂肪",width=100)
                tree.column("醣類",width=100)

                tree.heading("蛋白質",text="蛋白質")  #顯示錶頭
                tree.heading("脂肪",text="脂肪")
                tree.heading("醣類",text="醣類")

                tree.insert("",0,text="全穀根莖類" + str(total_consume[0]) + "份" ,values=(2*total_consume[0],"-",15*total_consume[0])) #插入資料，
                tree.insert("",1,text="蔬菜類" + str(total_consume[1]) + "份" ,values=(1*total_consume[1],"-",5*total_consume[1]))
                tree.insert("",2,text="水果類" + str(total_consume[2]) + "份" ,values=("-", "-", 15*total_consume[2]))
                tree.insert("",3,text="油脂與堅果種子類" + str(total_consume[3]) + "份" ,values=(1.5*total_consume[3],5*total_consume[3],"-"))
                tree.insert("",4,text="蛋豆魚肉類(高脂)" + str(total_consume[4]) + "份" ,values=(7*total_consume[4], 3*total_consume[4], "-"))
                tree.insert("",5,text="蛋豆魚肉類(中脂)" + str(total_consume[5]) + "份" ,values=(7*total_consume[5], 5*total_consume[5], "-"))
                tree.insert("",6,text="蛋豆魚肉類(低脂)" + str(total_consume[6]) + "份" ,values=(7*total_consume[6],10*total_consume[6],12*total_consume[6]))
                tree.insert("",7,text="奶類(全脂)" + str(total_consume[7]) + "份" ,values=(8*total_consume[7],8*total_consume[7],12*total_consume[7]))
                tree.insert("",8,text="奶類(低脂" + str(total_consume[8]) + "份" ,values=(8*total_consume[8],4*total_consume[8],12*total_consume[8]))
                tree.insert("",9,text="奶類(脫脂)" + str(total_consume[9]) + "份" ,values=(8*total_consume[9],"-",12*total_consume[9]))

                tree.pack()



        p2 = Page2()
        p2.master.title("My Nutrition Calculator")
        p2.mainloop()







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



