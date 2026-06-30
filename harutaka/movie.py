import sys
import csv

DATA_FILE = "movies.csv"

def init_file():
    """movies.csv が存在しない場合は、新規作成する"""
    try:
        with open(DATA_FILE, "a", encoding="utf-8") as f:
            pass
    except IOError:
        print(f"エラー: {DATA_FILE} の初期化に失敗しました。")

def load_data():
    """movies.csv から既存データを読み込む"""
    data = {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row or row[0].strip().lower() == "title":
                    continue
                if len(row) >= 4:
                    data[row[0].strip()] = {
                        "genre": row[1].strip(),
                        "rating": row[2].strip(),
                        "comment": row[3].strip()
                    }
    except FileNotFoundError:
        pass

    return data

def save_data(data):
    """データを movies.csv に保存する"""
    with open(DATA_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "genre", "rating", "comment"])
        for title, info in data.items():
            writer.writerow([
                title,
                info["genre"],
                info["rating"],
                info["comment"]
            ])

def main():
    init_file()

    args = sys.argv[2:]
    if len(sys.argv) < 2 or sys.argv[1].lower() != "add":
        print("使い方:")
        print("  python movie.py add <title> [ジャンル] [評価]")
        print("  python movie.py add [title] <ジャンル> <評価>")
        return

    data = load_data()

    title = ""
    genre = ""
    rating = ""
    comment = ""

    if len(args) >= 3:
        title = args[0].strip()
        genre = args[1].strip()
        rating = args[2].strip()
    elif len(args) == 1:
        title = args[0].strip()
    try:
        if not title:
            title = input("映画タイトルを入力してください：").strip()
        if not genre:
            genre = input(f"映画「{title}」のジャンルを入力してください：").strip()
        if not rating:
            rating = input(f"映画「{title}」の評価を入力してください（1～5）：").strip()

        comment = input(f"映画「{title}」の感想を入力してください：").strip()

    except (KeyboardInterrupt, EOFError):
        print("\n入力をキャンセルしました。")
        return

    if not title or not genre or not rating:
        print("エラー：タイトル、ジャンル、評価を入力する必要があります。")
        return

    if title in data:
        print(f"エラー：'{title}' は既に登録されています。")
        return

    data[title] = {
        "genre": genre,
        "rating": rating,
        "comment": comment
    }

    save_data(data)
    print(f"追加した（合計{len(data)}件)")

if__name__ == "__main__":
    main()
