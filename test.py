
import pyupbit

access = "ihNoglnZHTs8WAXFFXnkXQPx4lWk4Yxx9ae4YzNn"          # 본인 값으로 변경
secret = "zvoCx1H1cJnndeDDBlTYroNxX6HSPpQxH1xxLuXU"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-MOC"))     # KRW-MOC 조회 - 모스
print(upbit.get_balance("KRW-UPP"))     # KRW-UPP 조회 - 센티넬

print(upbit.get_balance("KRW"))         # 보유 현금 조회
