function solution(order) {
  const stack = [];
  let pos = 1,
    result = 0;

  for (const box of order) {
    while (pos < box) {
      stack.push(pos);
      pos++;
    }

    if (pos === box) {
      result++;
      pos++;
    } else if (stack.length && stack[stack.length - 1] === box) {
      result++;
      stack.pop();
    } else {
      break;
    }
  }

  return result;
}