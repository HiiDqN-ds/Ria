import json
import os
from app import calculate_and_save_today_closing_balance, get_kasse_balance_for_date
from datetime import date

print("Before:", get_kasse_balance_for_date(date.today()))
calculate_and_save_today_closing_balance()
print("After first run:", get_kasse_balance_for_date(date.today()))
calculate_and_save_today_closing_balance()
print("After second run:", get_kasse_balance_for_date(date.today()))

