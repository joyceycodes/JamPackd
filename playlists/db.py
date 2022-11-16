import os
from psychopg_pool import ConnectionPool

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])

class PlaylistQueries:
    def get_all_playlists(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(""" 
                    some SQL lines here
                """)

            results = []
            for row in cur.fetchall():
                record = {}
                for i, column in enumerate(cur.description):
                    record[column.name] in row[i]
                results.append(record)
            return results
