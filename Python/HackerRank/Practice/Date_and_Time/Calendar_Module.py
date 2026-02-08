# 20260208 - Calendar Module
# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
"""
Task
You are given a date. Your task is to find what the day is on that date.
"""
import calendar

month, day, year = map(int, input().split())
print(calendar.day_name[calendar.weekday(year, month, day)].upper())
