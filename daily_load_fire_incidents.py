import duckdb 
import pandas as pd
import schedule
import time

def update_fire_incidents():
    """
    Function to load the latest data and update the DuckDB table
    """    
    # Load the updated fire incidents CSV file
    fire_incidents_df = pd.read_csv('Fire_Incidents_20241030.csv')
    
    # Connect to DuckDB (using the existing database file 'fire_incidents.duckdb')
    con = duckdb.connect('fire_incidents.duckdb')
    
    # Replace the existing fire_incidents table with the updated data
    con.execute('DROP TABLE IF EXISTS fire_incidents')
    con.execute('CREATE TABLE fire_incidents AS SELECT * FROM fire_incidents_df')
    
    # Close the connection
    con.close()
    
# Schedule the update function to run daily at 1 AM
schedule.every().day.at("01:00").do(update_fire_incidents)

