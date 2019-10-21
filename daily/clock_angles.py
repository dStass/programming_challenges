'''
Problem: Angles of a Clock
From: Coding Interview Pro 18/10/2019

Given a time in the format of hour and minute,
calculate the angle of the hour and minute hand on a clock.
'''

def calcAngle(h, m):
  REVOLUTION = 360  # 360 degrees in a revolution
  TOTAL_HOURS = 12 # 12 hours on a clock
  TOTAL_MINUTES = 60 # 60 minutes on a clock
  h %= TOTAL_HOURS
  m %= TOTAL_MINUTES

  m_ratio = m/TOTAL_MINUTES
  m_angle = REVOLUTION * m_ratio
  h_ratio = h/TOTAL_HOURS
  h_angle = REVOLUTION * h_ratio # base hour
  h_angle += REVOLUTION * (1/TOTAL_HOURS) * m_ratio # hour hand based on minute hand
  h_angle %= REVOLUTION # mod 360 total angles
  return abs(m_angle - h_angle)

print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165
