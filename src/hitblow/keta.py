def select_digits():
    """遊ぶ桁数を入力してもらう"""
    while True:
        value = input("何桁で遊びますか？（3～9） > ").strip()

        if not value.isdigit():
            print("数字を入力してください。")
            continue

        digits = int(value)

        if 3 <= digits <= 9:
            return digits

        print("3～9の数字を入力してください。")