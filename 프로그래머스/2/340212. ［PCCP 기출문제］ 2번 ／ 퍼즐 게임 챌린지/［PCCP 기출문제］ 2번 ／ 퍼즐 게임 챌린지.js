function solution(diffs, times, limit) {
  let left = 1,
    right = 100000,
    mid = 0;

  while (left < right) {
    mid = Math.floor((left + right) / 2);

    const solved = solve(mid, diffs, times);

    if (solved <= limit) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }

  return left;
}

function solve(level, diffs, times) {
  let result = 0;

  diffs.forEach((diff, pos) => {
    const time_cur = times[pos];

    if (diff > level) {
      if (pos)
        result += (time_cur + times[pos - 1]) * (diff - level) + time_cur;
      else result += time_cur * (diff - level) + time_cur;
    } else {
      result += time_cur;
    }
  });

  return result;
}