#!/usr/bin/env python3

import pandas as pd
#Population Total area
#Helsinki         643272     715.48
#Espoo            279044     528.03
#Tampere          231853     689.59
#Vantaa           223027     240.35
#Oulu             201810     3817.52
def cities():
    return pd.DataFrame({"Population": [643272, 279044, 231853, 223027, 201810], "Total area": [715.48, 528.03, 689.59, 240.35, 3817.52]}, index=["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"])
    
def main():
    print(cities())
    
    
if __name__ == "__main__":
    main()
