import pandas as pd
scores = [100, 97, 88, 91]
average = pd.Series(scores).max()
print(average)
# git push -f grigin main 은 주의가 필요함 (원격 리포지토리를 로컬 리포지토리로 덮어씀)