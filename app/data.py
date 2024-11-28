from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient
import pandas as pd
import certifi


class Database:
    def __init__(self):
        '''Establish connection with MongoDB'''

        load_dotenv()
        db_url=getenv("DB_URL")

        #Setup a try-except to handle errors more comfortably
        try:
            self.db=MongoClient(db_url, tlsCAFile=certifi.where())["DatabaseCluster"]
            print(f"Connected succesfully to '{self.db.name}'")
        except Exception as e:
            print("Error connecting to the database:", e)
            self.db = None



    def seed(self, amount: int = 1000):
        '''Create a collection to place the random Monsters data'''

        collection=self.db["Monsters"]
        monsters_to_place=[]

        for _ in range(amount):
            monster= Monster()
            monsters_dict= monster.to_dict()
            print(monsters_dict)
            monsters_to_place.append(monsters_dict)

        print(monsters_to_place)


        result = collection.insert_many(monsters_to_place)
        print(f"{amount} monsters have been added into the collection")

        # Log the number of documents inserted
        print(f"Inserted {len(result.inserted_ids)} documents into 'Monsters' collection.")



    def reset(self):
        '''Delete all the documents from the collection'''

        if self.db is None:
            print("No active database connection")
            return

        try:
            collection = self.db["Monsters"]
            delete_docs = collection.delete_many({})
            print(f"All documents have been deleted from the 'Monsters' collection")

        except Exception as e:
            print("Error ocurred while resseting the collection", e)


    def count(self) -> int:
        """Retrieving the count of Monsters"""

        if self.db is None:
            print("No active database connection")
            return 0

        try:
            collection = self.db['Monsters']
            m_count = collection.count_documents({})
            print(f"Monsters Count: {m_count}")

        except Exception as e:
            print("Error while counting the documents", e)
            return 0

        return m_count



    def dataframe(self) -> DataFrame:
        '''Converting the collection into dataframe format'''

        if self.db is None:
            print("No active database connection")

        try:
            collection = self.db["Monsters"]
            documents = collection.find({}, {"_id": False})

            documents_list = list(documents)

            df = pd.DataFrame(documents_list)
            df.reset_index(inplace=True)
            df.rename(columns={"index": ''}, inplace=True)


            return df

        except Exception as e:
            print(f"Error while converting collection into dataframe", e)
            return pd.DataFrame()


    def html_table(self) -> str:
        '''retrieve the dataframe a place it on html format'''


        df = self.dataframe()

        if df.empty:
            print("The collection is empty.")
            return None

        html_table = df.to_html(classes="table table-striped", index=False)

        return html_table