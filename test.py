import pyupbit

access = "MFJxofnxchSc0VnDWyh163jeof2xOu5gZ93tUzQq"          # 본인 값으로 변경
secret = "BRlhqs1YCMcXv2QKGwRMisLc6Fc9dOmmIdkT7W0D"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회