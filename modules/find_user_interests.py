try:
    import sqlite3
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler
    from collections import Counter
    from itertools import chain

except ImportError as error:
    # Colored error message with ANSI codes
    print("\033[1;33m""⚠️  Failed to import modules: ""\033[0m", error)

def find_user_interests(db_path, user_id):
    # Number of each feature to return
    top_n_genres = 6 
    top_n_keywords = 10

    # Giving weight to features as their value in the processing
    col1 = "user_rate"
    col2 = "liked"
    w1 = 0.75
    w2 = 0.25

    conn = sqlite3.connect(db_path)
    query = '''
    SELECT ud.user_id, ud.movie_id, ud.user_rate, ud.liked, ms.genres, ms.keywords
    FROM Users_data ud
    JOIN Movies_sorted ms ON ud.movie_id = ms.movie_id
    WHERE ud.user_id = ?
    '''
    df = pd.read_sql_query(query, conn, params=(user_id,))
    conn.close()

    return [g[0] for g in top_genres], [k[0] for k in top_keywords]
