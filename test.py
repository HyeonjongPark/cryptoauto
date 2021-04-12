
import pyupbit

access_key = open("./akey.txt", "r").readline()
secret_key = open("./skey.txt", "r").readline()
upbit = pyupbit.Upbit(access_key, secret_key)

print(upbit.get_balance("KRW-MOC"))     # KRW-MOC 조회 - 모스
print(upbit.get_balance("KRW-UPP"))     # KRW-UPP 조회 - 센티넬

print(upbit.get_balance("KRW"))         # 보유 현금 조회
