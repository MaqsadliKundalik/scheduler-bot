from datetime import datetime, timedelta, timezone

def analyze_send_posts_logic():
    """
    send_posts_task funksiyasining mantiqini tahlil qilish
    """
    
    print("=" * 70)
    print("SEND_POSTS_TASK FUNKSIYA TAHLILI")
    print("=" * 70)
    
    # Hozirgi vaqt (UTC)
    now = datetime.now(timezone.utc)
    print(f"\n📅 Hozirgi vaqt (UTC): {now}")
    
    print("\n" + "=" * 70)
    print("SENARIY 1: Foydalanuvchi 5 daqiqa avval ro'yxatdan o'tgan")
    print("           Post vaqti: 1 minut")
    print("=" * 70)
    
    # User 5 daqiqa avval ro'yxatdan o'tgan
    user_created_at = now - timedelta(minutes=5)
    post_send_time = timedelta(minutes=1)  # 1 minut
    
    # Mantiq: send_at = user.created_at + post.send_time + timedelta(minutes=1)
    send_at = user_created_at + post_send_time + timedelta(minutes=1)
    
    print(f"\n   User ro'yxatdan o'tgan: {user_created_at}")
    print(f"   Post yuborish vaqti: {post_send_time} (1 minut)")
    print(f"   Qo'shimcha: +1 minut")
    print(f"   send_at = {send_at}")
    print(f"   now     = {now}")
    print(f"\n   Shart: send_at <= now")
    print(f"   {send_at} <= {now}")
    print(f"   Farq: {(now - send_at).total_seconds()} sekund")
    
    if send_at <= now:
        print("   ✅ YUBORILADI: Vaqt yetib kelgan!")
    else:
        print("   ❌ YUBORILMAYDI: Vaqt hali yetmagan!")
    
    print("\n" + "=" * 70)
    print("SENARIY 2: Foydalanuvchi 30 soniya avval ro'yxatdan o'tgan")
    print("           Post vaqti: 1 minut")
    print("=" * 70)
    
    user_created_at = now - timedelta(seconds=30)
    post_send_time = timedelta(minutes=1)
    send_at = user_created_at + post_send_time + timedelta(minutes=1)
    
    print(f"\n   User ro'yxatdan o'tgan: {user_created_at}")
    print(f"   Post yuborish vaqti: {post_send_time}")
    print(f"   Qo'shimcha: +1 minut")
    print(f"   send_at = {send_at}")
    print(f"   now     = {now}")
    print(f"\n   Shart: send_at <= now")
    print(f"   Farq: {(now - send_at).total_seconds()} sekund")
    
    if send_at <= now:
        print("   ✅ YUBORILADI")
    else:
        print("   ❌ YUBORILMAYDI: Hali {} sekund kutish kerak".format(
            int((send_at - now).total_seconds())
        ))
    
    print("\n" + "=" * 70)
    print("SENARIY 3: Post 1 kun oldin yuborilgan, hozir 2 kun o'tgan")
    print("           O'chirish mantigi: 1 kun o'tgandan keyin o'chirish")
    print("=" * 70)
    
    viewed_at = now - timedelta(days=2)  # 2 kun avval ko'rilgan
    delete_after = timedelta(days=1)      # 1 kun o'tgandan keyin o'chirish
    delete_at = viewed_at + delete_after
    
    print(f"\n   Post ko'rilgan vaqt: {viewed_at}")
    print(f"   O'chirish kerak: {delete_after} o'tgandan keyin")
    print(f"   delete_at = {delete_at}")
    print(f"   now       = {now}")
    print(f"\n   Shart: delete_at <= now")
    print(f"   Farq: {(now - delete_at).total_seconds() / 86400:.1f} kun o'tgan")
    
    if delete_at <= now:
        print("   ✅ O'CHIRILADI: 1 kun o'tgan!")
    else:
        print("   ❌ O'CHIRILMAYDI: Hali vaqt yetmagan")
    
    print("\n" + "=" * 70)
    print("MUHIM NUQTALAR")
    print("=" * 70)
    
    issues = []
    
    print("\n1️⃣ QIYMAT: +1 minut qo'shimcha qo'shilmoqda")
    print("   Kod: send_at = user.created_at + post.send_time + timedelta(minutes=1)")
    print("   ⚠️  Demak, agar admin '1 minut' desa, aslida 2 minut kutiladi!")
    issues.append("Admin 1 minut desa, aslida 2 minut o'tgandan keyin yuboriladi")
    
    print("\n2️⃣ LOOP: Har 10 sekundda tekshiriladi")
    print("   await asyncio.sleep(10)")
    print("   ✅ Bu yaxshi - tez ishlaydi")
    
    print("\n3️⃣ EXCEPTION HANDLING:")
    print("   - TelegramForbiddenError: User o'chiriladi")
    print("   - TelegramRetryAfter: Kutib turadi")
    print("   ✅ To'g'ri amalga oshirilgan")
    
    print("\n4️⃣ DELETE LOGIC: 1 kun o'tgandan keyin o'chirish")
    print("   elif already_viewed.viewed_at + timedelta(days=1) <= now:")
    print("   ✅ Bu to'g'ri mantiq")
    
    print("\n" + "=" * 70)
    print("ANIQLANGAN MUAMMOLAR")
    print("=" * 70)
    
    for idx, issue in enumerate(issues, 1):
        print(f"\n❌ {idx}. {issue}")
    
    print("\n" + "=" * 70)
    print("TAVSIYALAR")
    print("=" * 70)
    
    print("\n1. Qo'shimcha +1 minutni olib tashlash:")
    print("   O'rniga: send_at = user.created_at + post.send_time")
    print("   Sabab: Admin qancha vaqt desayapti, shuncha vaqt bo'lishi kerak")
    
    print("\n2. Logging qo'shish:")
    print("   print(f'Xabar yuborildi: user={user.telegram_id}, post={post.id}')")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    analyze_send_posts_logic()
