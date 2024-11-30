from pymongo import MongoClient

URL = "mongodb://admin:password@mongo-db:27017/"


def add_sample_data():
    # MongoDBサーバーへの接続
    client = MongoClient(URL)  # ローカルサーバー
    # client = MongoClient("<MongoDBの接続URI>")  # クラウドの場合

    # データベースの選択
    db = client["other"]

    # コレクションの選択
    collection = db["mycollection"]

    # データの挿入
    data = {"name": "Alice", "age": 25, "city": "Tokyo"}
    insert_result = collection.insert_one(data)
    print(f"Inserted ID: {insert_result.inserted_id}")

    # データの取得
    for doc in collection.find():
        print(doc)

    # 接続を閉じる（必要に応じて）
    client.close()

def get_mongodb_names() -> list[str]:
    with MongoClient(URL) as client:
        return client.list_database_names()

def show_mongodb_records(db: str, collection_name: str):
    with MongoClient(URL) as client:
        db_ = client[db]  # データベース名を指定
        collection = db_[collection_name]  # コレクション名を指定
        for record in collection.find():
            print(record)
        

if __name__ == "__main__":

    # print(" ".join(get_mongodb_names()))
    show_mongodb_records("users", "mycollection")
