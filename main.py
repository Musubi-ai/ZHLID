from src.zhlid import load_model


model = load_model("model/ZHLID", device_map="auto")


text = [
    "「台灣愛與希望國際關懷協會」年度愛心晚會，昨（24）日晚間在台北舉行，王瞳與霸氣樂團、班鐵翔與孟慶而等齊聚受邀愛心獻唱演出，久違的張芸京驚喜現身台下，現場熱情粉絲擠爆，睽違四年再度與霸氣樂團受邀出席該協會演出，王瞳表示24日剛好是三年前艾成的告別式，選在今天與霸氣樂團演出，艾成不會缺席，與大家在舞台上熱情獻唱。"
]


res = model.predict(text)
print(res)


