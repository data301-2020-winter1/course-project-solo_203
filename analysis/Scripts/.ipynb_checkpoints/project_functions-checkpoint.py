
def load_and_process(url_or_path_to_csv_file):
    import pandas as pd
    
    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
       .drop(columns = ["importance1", "importance2", "xg1", 'xg2', 'nsxg1','nsxg2','adj_score1','adj_score2',            'proj_score1', 'proj_score2'])
       .dropna(subset = ['score1','score2'] ) 
       .rename(columns = {'score1':'score_homeTeam', 'score2': 'score_awayTeam', 'spi1': 'spi_homeTeam', 'spi2':          'spi_awayTeam'})
     )
    
    df2 = (
        df1
        .loc[df1['season']<= 2018]
        .reset_index(drop=True)
        .sort_values('date', ascending = True)
    )
       
    return df2