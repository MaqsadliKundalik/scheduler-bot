class Message_contents:
    waiting_for_name_prompt = """
Azizbek Zubaydullayevning bonus botiga xush kelibsiz!✨

❤️‍🔥Ingliz tilini oʻrganishga doir ajoyib kontentlarni kuzatish uchun @AzizbekZubaydullayev ga obuna boʻlishingiz mumkin! 

Marhamat, "Noldan 3 oyda B1 roadmap" videodarsini olish uchun ism familiyangizni yozing👇
"""

    waiting_for_phone_number_prompt = """
Marhamat, raqamingizni kiriting:
"""

    registration_complete = """
Tabriklaymiz, botda muvaffaqqiyatli ro'yhatdan o'tdingiz!🎉

Mana sovgalaringiz!✨
"""

    subscribe_prompt = """
Productive School botiga xush kelibsiz✨

🎁"Noldan 3 oygacha Roadmap"ga ega bo'lganingiz bilan tabriklaymiz!

Marhamat uni olish uchun asoschimiz kanaliga obuna boʻling👇
"""
    
    already_registered = """
Asosiy menyudasiz!
"""
    consult_msg = """
🎯Bepul konsultatsiya: 60 kunda 5 ta daraja individual Yo'l Xaritasi!

Ha, aynan Siz uchun moslashtirilgan!

Aynan siz – Ingliz tilini tez o'rgatish bo'yicha mutaxassis, o'quvchilari noldan 5.5 oyda <a href="https://t.me/Feedback_ProEdu/205"> 5.5 IELTS</a>, noldan 3 oyda <a href="https://t.me/Feedback_ProEdu/211">B1</a> olgan

🏆Azizbek Zubaydullayevning "Fast English" uslubining aynan Sizga moslashtirilgan Yo'l Xaritasiga ega bo'lishingiz mumkin!

Hoziroq ro'yhatdan o'tib, 30 minutlik Individual konsultatsiyaga (300 ming so'm qiymatli) Bepul ega bo'ling!

🤫Pssst! Tez natija xohlamaydiganlar formani to'ldirmasin:
"""
    check_sub_msg = """
Productive School botiga xush kelibsiz✨

🎁"Noldan 3 oygacha Roadmap"ga ega bo'lganingiz bilan tabriklaymiz!

Marhamat uni olish uchun asoschimiz kanaliga obuna boʻling👇
"""
    
    consultation_questions = {
        "age": "Yoshingiz nechida?",
        "education_or_work": "O'qish/ishingiz?",
        "question1": {
            "text": "Hozirda \"Fast English\" kursi oʻquvchisimisiz?",
            "options": {
                "yes": "Ha",
                "no": "Yo'q"
            }
        },
        "question2": {
            "text": "\"Noldan 3 oyda B1 tahlili & Roadmap\" videodarsini (32minutlik) ko'rdingizmi?",
            "options": {
                "yes": "Ha",
                "no": "Yo'q"
            }
        },
        # Qachon va qanday imtihon topshirmoqchisiz? Va qanday natija olmoqchisiz?

        "question3": "Qachon va qanday imtihon topshirmoqchisiz? Va qanday natija olmoqchisiz?",
        # 10 ballik shkalada, siz uchun ingliz tilini AYNI HOZIR o'rganish qanchalik muhim? 
        "question4": {
            "text": "10 ballik shkalada, siz uchun ingliz tilini AYNI HOZIR o'rganish qanchalik muhim?",
            "options": {
                "1-4": "1 - 4",
                "5-7": "5 - 7",
                "8-10": "8 - 10"
                }
        },
        # Ingliz tilida 3 oy ichida o'zingiz orzu qilgan natijaga erishish uchun oyiga tahminan qancha pul sarf qilishga tayyorsiz? 
        "question5": {
            "text": "Ingliz tilida 3 oy ichida o'zingiz orzu qilgan natijaga erishish uchun oyiga tahminan qancha pul sarf qilishga tayyorsiz?",
            "options": {
                "0-400": "400 minggacha",
                "300-400": "300 mingdan 400 minggacha",
                "450-600": "450 mingdan 600 minggacha",
                "600+": "600 mingdan ko'proq"
            }
        }
    }