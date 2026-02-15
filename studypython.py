# # # # # # # bag_space = 0
# # # # # # # if bag_space > 0:
# # # # # # #     print("捡起大电")
# # # # # # # else:
# # # # # # #     print("背包满了，疯狂标记队友让他捡")
 
# # # # # # damage = 500

# # # # # # if damage >=750:
# # # # # #     print("起飞！红色护甲！")
# # # # # # elif damage >=450:
# # # # # #     print("还行，紫色护甲")
# # # # # # elif damage >=150:
# # # # # #     print("勉强，蓝色护甲")
# # # # # # else :
# # # # # #     print("白甲，赶紧去劝架刷伤害")

# # # # # enemies = ["动力小子","恶灵","狗子"]
# # # # # for enemy in enemies:
# # # # #     print("发现敌人:" + enemy)

# # # # def heal(item):
# # # #     print("使用" + item +"恢复护甲")

# # # # heal("大电")
# # # # heal("小电")

# # # class legend:
# # #     def __init__(self,name,hp):
# # #         self.name = name
# # #         self.hp = hp

# # #     def run(self):
# # #         print (self.name + "正在打药并开始啦大电")

# # # p1 = legend("动力小子",100)

# # # p2 = legend("恶灵",100)

# # # p1.run()

# # # p2.run

# # thesis = {
# #     "title":"学生管理系统",
# #      "progress":"50"
# #      }


# # thesis["progress"] = "80"
# # thesis["author"] = "shaochuang"

# # print(thesis)

# import random

# apex_pack = ["白色-莫桑比克","蓝色-狗子皮肤","紫色-R99","金色-传家宝"]

# result = random.choice(apex_pack)

# print("你打开了箱子，结果是：")
# print(result)

try:
    user_input = input("请输入你的学号（数字）：")
    my_id = int(user_input)
    print(my_id)    
except:
    print("输入错误！学号必须是数字！")

  