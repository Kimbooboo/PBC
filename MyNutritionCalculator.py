import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image

typeList = ["全穀根莖類", "蔬菜類", "水果類", "油脂與堅果種子類","蛋豆魚肉類", "奶類"]
unit_cal_list = [70, 25, 60, 45, 75, 120]
this_meal_consume = [0, 0, 0, 0, 0, 0]
total_consume = [0, 0, 0, 0, 0, 0]
meal_consume = 0
calories_quota = 0
calories_per_day = 0
which_meal = 0


list1200 = [6,3,2,4,3,1.5]
list1500 = [10,3,2,4,4,1.5]
list1800 = [12,3,2,5,5,1.5]
list2000 = [12,4,3,6,6,1.5]
list2200 = [14,4,3.5,6,6,1.5]
list2500 = [16,5,4,7,7,1.5]
list2700 = [16,5,4,8,8,2]
suggest = [0,0,0,0,0,0]


class Nutrition(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()


    def createWidgets(self):
        f1 = tkFont.Font(size=16, family="微軟正黑體")
        self.var = tk.StringVar()

        # 問年齡
        self.ageAsk = tk.Label(self, text="請問您的年齡？/歲", height=1, width=20, font=f1)
        self.ageAsk.grid(row=0, column=0)
        # 輸入年齡
        self.ageReply = tk.Entry(self, width=8)
        self.ageReply.grid(row=0, column=1)
        # 還沒加上單位：歲

        # 問性別
        self.genderAsk = tk.Label(self, text="請問您的性別？", height=1, width=20, font=f1)
        self.genderAsk.grid(row=1, column=0)

        self.genderM = tk.Radiobutton(self, text="男", variable=self.var, value="男", font=f1)
        self.genderM.grid(row=1, column=2, sticky=W, padx= 20)
        self.genderF = tk.Radiobutton(self, text="女", variable=self.var, value="女", font=f1)
        self.genderF.grid(row=1, column=1, sticky=W)

        # 問身高

        self.heightAsk = tk.Label(self, text="請問您的身高？/公分", height=1, width=20, font=f1)
        self.heightAsk.grid(row=2, column=0)
        self.heightReply = tk.Entry(self, width=8)
        self.heightReply.grid(row=2, column=1)
        # 問體重
        self.weightAsk = tk.Label(self, text="請問您的體重？/公斤", height=1, width=20, font=f1)
        self.weightAsk.grid(row=3, column=0)
        self.weightReply = tk.Entry(self, width=8)
        self.weightReply.grid(row=3, column=1)
        # 問活動量
        self.activityAsk = tk.Label(self, text="請問您的活動量為以下何種型態？", height=1, font=f1)
        self.activityAsk.grid(row=4, column=0)
        self.activityReply = ttk.Combobox(self, values=["輕度活動量", "稍輕活動量", "中度活動量", "高度活動量"], width=8)
        self.activityReply.grid(row=4, column=1)

        # 顯示活動量
        self.activityShow = tk.Label(self, text="活動量定義參考：", font=f1)
        self.activityShow1 = tk.Label(self, text="輕度活動量：整日坐臥、沒有運動", font=f1)
        self.activityShow2 = tk.Label(self, text="稍輕活動量：整日多坐著、通勤有緩步", font=f1)
        self.activityShow3 = tk.Label(self, text="中度活動量：整日多站立、多走動", font=f1)
        self.activityShow4 = tk.Label(self, text="高度活動量：從事如運動員、搬運員等多勞動工作", font=f1)

        self.activityShow.grid(row=5, column=0, padx=20, sticky=W)
        self.activityShow1.grid(row=6, column=0, padx=20, sticky=W)
        self.activityShow2.grid(row=7, column=0, padx=20, sticky=W)
        self.activityShow3.grid(row=8, column=0, padx=20, sticky=W)
        self.activityShow4.grid(row=9, column=0, padx=20, sticky=W)
        self.calculator = tk.Button(self, text="計算您一天\n應攝取的熱量", command=self.click2calculateCalories, font=f1)
        self.calculator.grid(row=6, column=1, rowspan=3, columnspan=1)

    def record_gender(self):
        self.record_gender = self.var.get()

    def click2calculateCalories(self):

        height = float(self.heightReply.get())
        weight = float(self.weightReply.get())
        age = int(self.ageReply.get())
        activity = self.activityReply.get()
        gender = self.record_gender

        # 計算基礎代謝率
        if gender == "男":
            REE = 66 + (13.7 * weight) + (5.0 * height) - (6.8 * age)  # 10 * weight + 6.25 * height - 5 * age + 5
        else:
            REE = 655 + (9.6 * weight) + (1.7 * height) - (4.7 * age)  # 10 * weight + 6.25 * height - 5 * age - 161

        # 加上活動量，計算總共可攝取的熱量
        global calories_quota

        if activity == "輕度活動量":
            cal = int(REE * 1.0)
            calories_quota = cal
        elif activity == "稍輕活動量":
            cal = int(REE * 1.2)
            calories_quota = cal
        elif activity == "中度活動量":
            cal = int(REE * 1.375)
            calories_quota = cal
        elif activity == "高度活動量":
            cal = int(REE * 1.55)
            calories_quota = cal

        calories_per_day = calories_quota

        # 判斷這個人一天可攝取卡路里應該對照行政院飲食建議的哪個區間
        if 1200 < calories_quota <= 1500:
            for i in range(6):
                suggest[i] = list1200[i]
        elif 1500 < calories_quota <= 1800:
            for i in range(6):
                suggest[i] = list1500[i]
        elif 1800 < calories_quota <= 2000:
            for i in range(6):
                suggest[i] = list1800[i]
        elif 2000 < calories_quota <= 2200:
            for i in range(6):
                suggest[i] = list2000[i]
        elif 2200 < calories_quota <= 2500:
            for i in range(6):
                suggest[i] = list2200[i]
        elif 2500 < calories_quota <= 2700:
            for i in range(6):
                suggest[i] = list2500[i]
        elif 2700 < calories_quota:
            for i in range(6):
                suggest[i] = list2700[i]

        self.destroy()

        # 當user輸完基本資料，按下計算鍵才跳出Page2的輸入飲食
        class Page2(tk.Frame):
            def __init__(self):
                tk.Frame.__init__(self)
                self.grid()
                self.createWidgets()

            def createWidgets(self):

        # 調整字體
                import tkinter.font as tkFont
                f1 = tkFont.Font(size = 16, family = "微軟正黑體")
                f2 = tkFont.Font(size = 20, family = "微軟正黑體")
                f3 = tkFont.Font(size = 13, family = "微軟正黑體")

        #  標題
                self.Calories_quota_label = tk.Label(self, text = "本人今日熱量餘額為" + str(calories_quota) + "大卡", font = f2)
                self.Calories_quota_label.grid(row = 0, column = 0, columnspan=3)

                self.inputword = tk.Label(self, text="請開始依照六大類食物記錄您吃過的食物，\n若不清楚食物類別或份量，可點擊右方按鈕檢視參考圖", font=f1)
                self.inputword.grid(row=1, column=0, columnspan=2, pady=2)
                self.exampletitle = tk.Label(self, text="範例：假設您今天吃了一碗白飯，則輸入:", font=f1)
                self.exampletitle.grid(row=2, column=0, columnspan=2)
                self.example = tk.Label(self, text= "五穀根莖類 4 份（白飯一碗相當於四份）", font=f1)
                self.example.grid(row=3, column=0, columnspan=2)


        # 類別份數參考
                self.referenceBTN = tk.Button(self, text = "(類別份數參考圖)", font = f1, command = self.referenceImage)
                self.referenceBTN.grid(row = 1, column = 3, padx=5, sticky=E)
        
        # 食物類別選單
                self.type = tk.StringVar()
                self.type.set("食物類別")
                self.optionmenu = tk.OptionMenu(self, self.type, *typeList)
                self.optionmenu.grid(row = 4, column = 0, sticky=tk.E)
                self.optionmenu.config(font = f1)

        # 單位選擇
                self.unit = tk.Spinbox(self, from_=0, to=10, increment = 0.5, font = f1, width=10, text="份")
                self.unit.grid(row = 4, column = 1)
                unit_label = tk.Label(self, text = "份", font = f1)
                unit_label.grid(row = 4, column = 2)

        # 下一個食物
                self.sendfood = tk.Label(self, text= "按下'確定'鍵來送出食物品項！")
                self.sendfood.grid(row=3, column=3, columnspan=1)
                self.nxt_foodbtn = tk.Button(self, text = "確定", font = f1, command = self.nxt_food_cmd, foreground= "red")
                self.nxt_foodbtn.grid(row = 4, column = 3, columnspan=1)
        # 此餐統計
                self.end = tk.Label(self, text= "這次進食結束了嗎？\n那就按下'此餐統計'按鈕吧！")
                self.end.grid(row=6, column=3, columnspan=2, rowspan=1, pady=10)
                self.end_inputbtn = tk.Button(self, text = "此餐統計", font = f1, command = self.this_meal_sum)
                self.end_inputbtn.grid(row = 7, column = 3,columnspan=2)

        # 吃了甚麼
                self.eaten_label = tk.Label(self, text ="", font = f1)
                self.eaten_label.grid(row = 6, columnspan = 3)



        ### listener

            def referenceImage(self):
                referenceWindow = tk.Toplevel()
                referenceWindow.title("份數對照圖")
# 檔案路徑需更動
                ph = ImageTk.PhotoImage(file = "/Users/yijing/Desktop/份數對照.png")
                reference_label = tk.Label(referenceWindow, image = ph)
                reference_label.image = ph
                reference_label.pack()

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

                global which_meal
                global this_meal_consume
                global total_consume


        # 加進今日
                for i in range(6):
                    total_consume[i] += this_meal_consume[i]

        # 創表
                which_meal += 1
                p3 = tk.Toplevel()
                tree = ttk.Treeview(p3)
                p3.title("第" + str(which_meal) + "餐統計")
                tree["columns"]=("此餐攝取/已攝取/建議攝取(份)","蛋白質/克","脂肪/克","醣類/克","熱量/大卡")
                tree.column("此餐攝取/已攝取/建議攝取(份)",width=150)    #表示列,不顯示
                tree.column("蛋白質/克",width=100)
                tree.column("脂肪/克",width=100)
                tree.column("醣類/克",width=100)
                tree.column("熱量/大卡",width=100)

                tree.heading("此餐攝取/已攝取/建議攝取(份)",text="此餐攝取/已攝取/建議攝取(份)")
                tree.heading("蛋白質/克",text="蛋白質/克")  #顯示錶頭
                tree.heading("脂肪/克",text="脂肪/克")
                tree.heading("醣類/克",text="醣類/克")
                tree.heading("熱量/大卡",text="熱量/大卡")

                tree.insert("",0,text="全穀根莖類",values=(str(this_meal_consume[0])+"    /    "+ str(total_consume[0]) + "    /    " +str(suggest[0]), 2*this_meal_consume[0],"-",15*this_meal_consume[0], unit_cal_list[0]*this_meal_consume[0]))
                tree.insert("",1,text="蔬菜類",values=(str(this_meal_consume[1])+"    /    "+ str(total_consume[1]) + "    /    " +str(suggest[1]), 1*this_meal_consume[1],"-",5*this_meal_consume[1], unit_cal_list[1]*this_meal_consume[1]))
                tree.insert("",2,text="水果類",values=(str(this_meal_consume[2])+"    /    "+ str(total_consume[2]) + "    /    " +str(suggest[2]), "-", "-", 15*this_meal_consume[2], unit_cal_list[2]*this_meal_consume[2]))
                tree.insert("",3,text="油脂與堅果種子類",values=(str(this_meal_consume[3])+"    /    "+ str(total_consume[3]) + "    /    " +str(suggest[3]),"-",5*this_meal_consume[3],"-", unit_cal_list[3]*this_meal_consume[3]))
                tree.insert("",4,text="蛋豆魚肉類",values=(str(this_meal_consume[4])+"    /    "+ str(total_consume[4]) + "    /    " +str(suggest[4]), 7*this_meal_consume[4], 5*this_meal_consume[4], "-", unit_cal_list[4]*this_meal_consume[4]))
                tree.insert("",5,text="奶類",values=(str(this_meal_consume[5])+"    /    "+ str(total_consume[5]) + "    /    " +str(suggest[5]), 8*this_meal_consume[5],4*this_meal_consume[5],12*this_meal_consume[5], unit_cal_list[5]*this_meal_consume[5]))

                protein_sum = 2*this_meal_consume[0] + 1*this_meal_consume[1] + 7*this_meal_consume[4] + 8*this_meal_consume[5]
                fat_sum = 5*this_meal_consume[3] + 5*this_meal_consume[4] + 4*this_meal_consume[5]
                CH_sum = 15*this_meal_consume[0] + 5*this_meal_consume[1] + 15*this_meal_consume[2] + 12*this_meal_consume[5]
                Cal_sum = unit_cal_list[0]*this_meal_consume[0] + unit_cal_list[1]*this_meal_consume[1]+ unit_cal_list[2]*this_meal_consume[2]+ unit_cal_list[3]*this_meal_consume[3]+ unit_cal_list[4]*this_meal_consume[4]+ unit_cal_list[5]*this_meal_consume[5]
                tree.insert("",6,text="總計",values=("-", protein_sum, fat_sum, CH_sum, Cal_sum))
                tree.pack()

        # 運算
                global meal_consume

                global calories_quota
                self.Calories_quota_label.configure(text = "本人今日熱量餘額為" + str(calories_quota - meal_consume) + "大卡")

                calories_quota -= meal_consume
                meal_consume = 0

        # 此餐歸零
                for i in range(6):
                    this_meal_consume[i] = 0


        # 清除此餐內容
                self.eaten_label.configure(text ="")


        # 今日結算按鈕
                import tkinter.font as tkFont
                f1 = tkFont.Font(size = 16, family = "微軟正黑體")
                self.today_sumtitle = tk.Label(self, text="今天確定不會再吃東西了嗎？\n那就按下'今日結算'來看看今天的飲食有沒有營養均衡吧！")
                self.today_sumtitle.grid(row=8,column=0, columnspan=2, sticky=E)
                self.today_sum_btn = tk.Button(self, text = "今日結算", font = f1, command = self.TDSum_Cmd)
                self.today_sum_btn.grid(row = 8,column=3, pady=10)


            def TDSum_Cmd(self):

                for i in range(6):
                    total_consume[i] += this_meal_consume[i]
                    this_meal_consume[i] = 0

                p4 = tk.Toplevel()
                tree = ttk.Treeview(p4)
                p4.title("今日統計")
                tree["columns"]=("今日攝取/建議攝取(份)","蛋白質/克","脂肪/克","醣類/克","熱量/大卡")
                tree.column("今日攝取/建議攝取(份)",width=130)    #表示列,不顯示
                tree.column("蛋白質/克",width=100)
                tree.column("脂肪/克",width=100)
                tree.column("醣類/克",width=100)
                tree.column("熱量/大卡",width=100)

                tree.heading("今日攝取/建議攝取(份)",text="今日攝取/建議攝取(份)")
                tree.heading("蛋白質/克",text="蛋白質/克")  #顯示錶頭
                tree.heading("脂肪/克",text="脂肪/克")
                tree.heading("醣類/克",text="醣類/克")
                tree.heading("熱量/大卡",text="熱量/大卡")

                tree.insert("",0,text="全穀根莖類",values=(str(total_consume[0])+"    /    "+str(suggest[0]), 2*total_consume[0],"-",15*total_consume[0], unit_cal_list[0]*total_consume[0])) #插入資料，
                tree.insert("",1,text="蔬菜類",values=(str(total_consume[1])+"    /    "+str(suggest[1]), 1*total_consume[1],"-",5*total_consume[1], unit_cal_list[1]*total_consume[1]))
                tree.insert("",2,text="水果類",values=(str(total_consume[2])+"    /    "+str(suggest[2]), "-", "-", 15*total_consume[2], unit_cal_list[2]*total_consume[2]))
                tree.insert("",3,text="油脂與堅果種子類",values=(str(total_consume[3])+"    /    "+str(suggest[3]), 1.5*total_consume[3],5*total_consume[3],"-", unit_cal_list[3]*total_consume[3]))
                tree.insert("",4,text="蛋豆魚肉類",values=(str(total_consume[4])+"    /    "+str(suggest[4]), 7*total_consume[4], 5*total_consume[4], "-", unit_cal_list[4]*total_consume[4]))
                tree.insert("",5,text="奶類",values=(str(total_consume[5])+"    /    "+str(suggest[5]), 8*total_consume[5],4*total_consume[5],12*total_consume[5], unit_cal_list[5]*total_consume[5]))

                protein_sum = 2*total_consume[0] + 1*total_consume[1] + 7*total_consume[4] + 8*total_consume[5]
                fat_sum = 5*total_consume[3] + 5*total_consume[4] + 4*total_consume[5]
                CH_sum = 15*total_consume[0] + 5*total_consume[1] + 15*total_consume[2] + 12*total_consume[5]
                Cal_sum = unit_cal_list[0]*total_consume[0] + unit_cal_list[1]*total_consume[1]+ unit_cal_list[2]*total_consume[2]+ unit_cal_list[3]*total_consume[3]+ unit_cal_list[4]*total_consume[4]+ unit_cal_list[5]*total_consume[5]
                tree.insert("",6,text="總計",values=("-", protein_sum, fat_sum, CH_sum, str(Cal_sum)+" / "+str(calories_per_day)))
                tree.grid(row=0,column=0)
                
                '''給予今日飲食評論'''
                lack = list()
                excess = list()
                for i in range(len(typeList)):
                    if total_consume[i] < suggest[i]:
                        lack.append(typeList[i])
                    elif total_consume[i] > suggest[i]:
                        excess.append(typeList[i])
                
                # 吃不夠份量的食物類別
                if lack:
                    if len(lack)>1:
                        temp = "、".join(lack)
                    else:
                        temp = lack[0]
                    review = "今天的"+ str(temp)+ "好像不太夠哦！"
                    lacklabel = tk.Label(p4, text=review)
                    lacklabel.grid(row=1, columnspan=1)
                # 吃太多的食物類別
                if excess:
                    if len(excess)>1:
                        temp = "、".join(excess)
                    else:
                        temp = excess[0]
                    review = "今天的"+ str(temp)+ "好像吃太多了！"
                    excesslabel = tk.Label(p4, text=review)
                    excesslabel.grid(row=2, columnspan=1)
                # 吃得剛剛好
                if len(lack) == 0 and len(excess) == 0:
                    goodjob = tk.Label(p4, text="今天的飲食超均衡的耶！")
                    goodjob.grid(row=1, columnspan=1)
                
                # 整體熱量評論
                if Cal_sum > calories_per_day:
                    cal_label = tk.Label(p4, text="整體攝取的熱量好像太多了哦～要注意一下～")
                    cal_label.grid(row=3, columnspan=1)
                elif Cal_sum < calories_per_day:
                    cal_label = tk.Label(p4, text= "整體攝取的熱量好像還少了一些～要不要再吃點東西呀？")
                    cal_label.grid(row=3, columnspan=1)
                elif Cal_sum < calories_per_day:
                    cal_label = tk.Label(p4, text="今天攝取的熱量很剛好耶～繼續保持！")
                    cal_label.grid(row=3, columnspan=1)

        p2 = Page2()
        p2.master.title("My Nutrition Calculator")
        p2.mainloop()


nutri = Nutrition()
nutri.master.title("My Nutrition Calculator")
nutri.mainloop()



