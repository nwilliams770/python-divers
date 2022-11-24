def _count(arr, i):
  count = 0

  for j in range(i, len(arr)):
    if arr[i] >= arr[j]:
      count += 1
    else:
      break;

  for j in range(i - 1, -1, -1):
    if arr[i] >= arr[j]:
      count += 1
    else:
      break;

  return count


def count_subarrays(arr):
  # Write your code here
  n = len(arr)
  result = []

  for i in range(n):
    result.append(_count(arr, i))


  return result
