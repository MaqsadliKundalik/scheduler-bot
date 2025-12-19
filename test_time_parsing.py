import re
from datetime import timedelta

def test_time_parsing(text):
    """Test time parsing logic"""
    text = text.strip().lower()
    
    # Default qiymatlar - nima aytilmasa 0
    days = hours = minutes = 0

    # Kun, soat, minut qiymatlarini qidirish
    day_match = re.search(r'(\d+)\s*kun', text)
    hour_match = re.search(r'(\d+)\s*soat', text)
    minute_match = re.search(r'(\d+)\s*minut', text)

    if day_match:
        days = int(day_match.group(1))
    if hour_match:
        hours = int(hour_match.group(1))
    if minute_match:
        minutes = int(minute_match.group(1))

    # Jami sekundlarni hisoblash
    total_seconds = days * 86400 + hours * 3600 + minutes * 60
    
    # Timedelta yaratish
    send_time = timedelta(seconds=total_seconds)
    
    return {
        'input': text,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'total_seconds': total_seconds,
        'timedelta': send_time,
        'timedelta_str': str(send_time)
    }

# Test cases
test_cases = [
    "1 minut",
    "2 soat",
    "1 kun",
    "1 kun 20 soat 30 minut",
    "30 minut",
    "5 kun 12 soat",
    "15 minut",
]

print("=" * 60)
print("TIME PARSING TEST")
print("=" * 60)

for test in test_cases:
    result = test_time_parsing(test)
    print(f"\n📝 Input: '{result['input']}'")
    print(f"   Kun: {result['days']}, Soat: {result['hours']}, Minut: {result['minutes']}")
    print(f"   Jami: {result['total_seconds']} sekund")
    print(f"   Timedelta: {result['timedelta_str']}")
    
    # Tekshirish
    if test == "1 minut":
        assert result['total_seconds'] == 60, "❌ 1 minut = 60 sekund bo'lishi kerak!"
        assert result['minutes'] == 1, "❌ minutes = 1 bo'lishi kerak!"
        print("   ✅ TO'G'RI!")
    elif test == "2 soat":
        assert result['total_seconds'] == 7200, "❌ 2 soat = 7200 sekund bo'lishi kerak!"
        print("   ✅ TO'G'RI!")
    elif test == "1 kun":
        assert result['total_seconds'] == 86400, "❌ 1 kun = 86400 sekund bo'lishi kerak!"
        print("   ✅ TO'G'RI!")

print("\n" + "=" * 60)
print("✅ BARCHA TESTLAR MUVAFFAQIYATLI O'TDI!")
print("=" * 60)
