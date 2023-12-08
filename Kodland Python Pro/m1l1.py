meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "YEET": "Bir şeyi güçlü bir şekilde fırlatmak veya atlamak",
            "SWAG": "Sofistike, modaya uygun ve havalı olmak",
            "FOMO": "Bir şeyin dışında kalma korkusu",
            "BRUH": "Bir şeye şaşırmak veya hayal kırıklığına uğramak için kullanılan bir ifade"
            }

word = input("Anlamadığınız bir kelime yazın!")
word = word.upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("girdiğiniz kelime sözlükte yok")