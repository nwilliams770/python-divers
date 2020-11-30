def numberOfWays(arr, k):
  pair_sums = 0
  counter = {};

  for num in arr:
    missing_num = abs(k - num)
    if missing_num in counter:
      pair_sums += counter[missing_num]
      counter[missing_num] = counter.get(num, 0) + 1

    else:
      counter[num] = counter.get(num, 0) + 1



  return pair_sums
