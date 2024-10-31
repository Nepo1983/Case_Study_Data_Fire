import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import duckdb
from daily_load_fire_incidents import update_fire_incidents

class TestUpdateFireIncidents(unittest.TestCase):

    @patch('daily_load_fire_incidents.pd.read_csv')
    @patch('daily_load_fire_incidents.duckdb.connect')
    def test_update_fire_incidents(self, mock_connect, mock_read_csv):
        # Mock the read_csv function to return a sample dataframe
        sample_data = {'column1': [1, 2], 'column2': [3, 4]}
        mock_read_csv.return_value = pd.DataFrame(sample_data)
        
        # Mock the DuckDB connection and cursor
        mock_con = MagicMock()
        mock_connect.return_value = mock_con
        
        # Call the function to test
        update_fire_incidents()
        
        # Check if read_csv was called with the correct file name
        mock_read_csv.assert_called_once_with('Fire_Incidents_20241030.csv')
        
        # Check if DuckDB connect was called with the correct database file
        mock_connect.assert_called_once_with('fire_incidents.duckdb')
        
        # Check if the correct SQL commands were executed
        mock_con.execute.assert_any_call('DROP TABLE IF EXISTS fire_incidents')
        mock_con.execute.assert_any_call('CREATE TABLE fire_incidents AS SELECT * FROM fire_incidents_df')
        
        # Check if the connection was closed
        mock_con.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()